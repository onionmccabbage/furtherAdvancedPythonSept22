# consider a laptop which can be in one of these states: ON, OFF, SLEEP amd HYBERNATE
# we can go from ON to OFF, ON to SLEEP but not OFF to SLEEP

class ComputerState():
    name = 'state'
    allowed = [] # this list will contain the permitted states
    def switch(self, state):
        if state.name in self.allowed:
            print('Current state {} switching top {}'.format(self, state.name))
            self.__class__ = state # make hte state change
        else:
            print('Current state {} cannot switch to {}'.format(self, state.name))
    def __str__(self):
        return self.name

