import threading
import time

# here are some globals
counter = 1 # this global asset can be accessed by every thread - we will need to lock access
lock = threading.Lock() # we now have a lock we can use

def workerA():
    global counter # we need access to the global asset
    lock.acquire()
    try:
        while counter <100: # try to increment up to +100
            counter += 1 # increment
            print('Worker A increments counter to {}'.format(counter))
    except Exception as e:
        print(e)
    finally:
        lock.release() # release the lock when we no longer need it
        pass

def workerB():
    global counter # we need access to the global asset
    lock.acquire()
    try:
        while counter >-100: # try to decrement all the way to -100
            counter -= 1 # decrement
            print('Worker B decrements counter to {}'.format(counter))
    except Exception as e:
        print(e)
    finally:
        lock.release() # release the lock when we no longer need it   
        pass

if __name__ == '__main__':
    # we can measure how long code takes to execute
    t0 = time.time()
    thread1 = threading.Thread(target=workerA)
    thread2 = threading.Thread(target=workerB)
    thread2.start()
    thread1.start() # it can make a difference the order in which locked threads are started
    thread1.join()
    thread2.join()
    t1 = time.time()
    print('total execution time {} seconds'.format(t1-t0)) # always a good idea to take repeated measurements