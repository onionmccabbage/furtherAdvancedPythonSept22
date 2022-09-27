from threading import Thread
from random import random
import time
import sys

# create a normal class (which our threa will call)
class MyClass: # NB this does NOT inherit from Thread
    def __call__(self, name): # we now have a callable class - 'Thread' can call it
        for i in range(1,50):
            time.sleep(random()*0.1)
            print(name)

if __name__ == '__main__':
    # make some isntances of our class
    m1 = MyClass()
    m2 = MyClass()
    # make some threads
    t1 = Thread(target=m1, args=('t1',))
    t2 = Thread(target=m2, args=('t2',))
    t1.start()
    t2.start()
    t1.join()
    t2.join()