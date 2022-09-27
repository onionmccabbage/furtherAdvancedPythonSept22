import threading
import time

# here are some globals
counter = 1 # this global asset can be accessed by every thread - we will need to lock access
lock = threading.Lock() # we now have a lock we can use

def workerA():
    global counter # we need access to the global asset
    lock.acquire()
    try:
        while counter <100:
            counter += 1 # increment
            print('Worker A increments coutnerr to {}'.format(counter))
    except Exception as e:
        print(e)
    finally:
        lock.release() # release the lock when we no longer need it
        