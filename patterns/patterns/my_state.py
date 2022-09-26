# consider a laptop which can be in one of these states: ON, OFF, SLEEP amd HYBERNATE
# we can go from ON to OFF, ON to SLEEP but not OFF to SLEEP

class ComputerState():
    name = 'state'
    allowed = [] # this list will contain the permitted states
    def switch(self, state):
        if state.name in self.allowed:
            print('Current state {} switching to {}'.format(self, state.name))
            self.__class__ = state # make hte state change
        else:
            print('Current state {} cannot switch to {}'.format(self, state.name))
    def __str__(self):
        return self.name

class On(ComputerState):
    name = 'on'
    allowed = ['off', 'sleep', 'hybernate']

class Off(ComputerState):
    name='off'
    allowed = ['on']

class Sleep(ComputerState):
    name='sleep'
    allowed = ['on']

class Hybernate(ComputerState):
    name='hybernate'
    allowed = ['on']

class Computer():
    def __init__(self, model):
        self.model = model
        self.state = Off()
    def change(self, change_to):
        self.state.switch(change_to)

if __name__ == '__main__':
    comp = Computer('wizzy') # initially the computer  will be 'Off'
    comp.change(On)
    comp.change(Off)
    comp.change(On)
    comp.change(Sleep)
    comp.change(On)
    comp.change(Hybernate)
    comp.change(Sleep) # not a permitted state change
