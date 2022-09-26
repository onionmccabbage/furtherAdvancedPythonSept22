# use a factory to manufacture items
from abc import abstractmethod

class Animal():
    @abstractmethod # this is a decorator
    def do_say(self):
        pass

class Dog(Animal):
    def do_say(self):
        print('woof')

class Cat(Animal):
    def do_say(self):
        print('miaow')

class Bat(Animal):
    def do_say(self):
        print('____')   

# a factory to create animals
class CreatureFactory():
    def make_sound(self, object_type):
        return eval(object_type)().do_say() # this returns a call to an instance of a creature

if __name__ == '__main__':
    cf = CreatureFactory() # we now have an instance of our factory
    animal = input('Which creature? ')
    cf.make_sound(animal)