from threading import Lock # the Lock class is a Lock factory

# here is a custom decorator to make a class thread-safe with Locks
def lock_a_class(method_names, lock_factory):
    return lambda cls:make_thread_safe(cls, method_names, lock_factory)

def lock_a_method(meth):
    if getattr(meth, '__is_locked', False): # only lock methods that are not already locked
        raise TypeError('Method {} is already locked'.format(meth))
    def locked_method(self, *args, **kwargs):
        with self.__lock: # using 'with' will release the lock when done
            return meth(self, *args, **kwargs)
    lock_a_method.__name__ = '{} ({})'.format('Locked Method', meth.__name__)
    locked_method.__is_locked = True
    return locked_method

def make_thread_safe(cls, method_names, lock_factory):
    init = cls.__init__ # take a copy of the exisiting init method of the decorated class
    def new_init(self, *args, **kwargs):
        init(self, *args, **kwargs)
        self.__lock = lock_factory
    cls.__init__ = new_init # our decorated class has a fresh init method
    # iterate over all the clas methods making each thread safe with locks
    for methodN in method_names:
        old_meth = getattr(cls, methodN)
        new_meth = lock_a_method(old_meth)
        setattr(cls, methodN, new_meth)
    return cls # return the modified class

# here we apply our decorator to lock a class.
# this class will inherit from 'set' then we overide hte built-in 'add' and 'remove'
# members of a set
@lock_a_class(['add', 'remove'], Lock)
class Myclass(set):
    pass

if __name__ == '__main__':
    my_set = (4,3,2)
    my_inst = Myclass(my_set)
    # is it locked?
    print(my_inst.add.__is_locked) # True
    print(my_inst.remove.__is_locked) # True
