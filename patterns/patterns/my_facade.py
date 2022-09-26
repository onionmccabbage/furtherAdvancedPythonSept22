# a facade sits in front of the actual bits thatt are related
# here we need a coder, a tester, a techincian, an artisan and a manager
# we can declare them all as abstract non-inter-dependent classes

class Coder():
    def __init__(self):
        print('write some code')
    def __is_available__(self):
        print('coding skills are available')
        return True
    def book_time(self):
        if self.__is_available__():
            print('coder has been booked')

class Tester():
    def __init__(self):
        print('preparing tests')
    def testing(self):
        print('tests are in place')

class Technician():
    def __init__(self):
        print('Prparing equipment for the team')
    def do_stuff(self):
        print('network, machines and stuff are in place')

class Artisan():
    def __init__(self):
        print('designing things')
    def make_prototype(self):
        print('wireframes are ready')

class Manager(): # this is the facade for all the other skills
    def __init__(self):
        print('Manager says I can arrange the team')
    def arrange(self):
        # the facade needs to provide instances of all the subsystems (could be microservices, pools, toolchains etc.)
        self.coder = Coder()
        self.tester = Tester()
        self.technician = Technician()
        self.artisan = Artisan()
        # put them to work
        self.coder.book_time()
        self.tester.testing()
        self.technician.do_stuff()
        self.artisan.make_prototype()

class Client(): # the client that will make use of the facade
    def __init__(self):
        print('we need a team...')
    def askManager(self):
        print('Lets ask the manager ...') # here we invoke the facade
        m = Manager() # or self.m = Manager()
        m.arrange()  
    def __del__(self): # all classes will run this if the override is provided
        print('all done')

if __name__ == '__main__':
    you = Client()
    you.askManager()