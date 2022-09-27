# using re-entrant locks (rlocks)
# if a thread already has access to an rlock it cana use it more efficiently
import threading
import time
import sys

# we could use classes or functions for our thread
class MyWorker():
    def __init__(self):
        self.a = 1
        self.b = 2
        self.rlock = threading.RLock() # here we are providing a re-entrant lock for this class
    def modifyA(self):
        with self.rlock: # using 'with' will automatically release the lock when done
            sys.stdout.write('Rlock acquired {}, modifying A\n'.format(self.rlock._is_owned()))
            # we can examine the RLock
            sys.stdout.write(''.format(self.rlock))
            self.a +=1
            time.sleep(2)
    def modifyB(self):
        with self.rlock: # using 'with' will automatically release the lock when done
            sys.stdout.write('Rlock acquired {}, modifying B\n'.format(self.rlock._is_owned()))
            # we can examine the RLock
            sys.stdout.write(''.format(self.rlock))
            self.b -=1
            time.sleep(2)
    def modifyBoth(self):
        self.modifyB()
        self.modifyA()

if __name__ == '__main__':
    worker = MyWorker()
    worker.modifyA()
    worker.modifyB()
    worker.modifyBoth()
