# threads can be defined by functions or by classes
import random
import threading
import time
# each thread has a life cycle
def threadWorker(): # this function is callable to run in as many threads as we like
    print('thread is running')
    time.sleep(2)
    print('thread is terminating') # this is implicitly the end of the function so implicitly the 'return'

def executeThread(i): # here we pass in an argument
    print('Thread {} has started'.format(i))
    sleepTime = random.randint(1,4)
    time.sleep(sleepTime)
    print('Thread {} has finished executing'.format(i))

if __name__ == '__main__':
    myThread = threading.Thread(target=threadWorker)
    myThread.start() # the function will execute on its own separate thread
    myThread.join() # best practice to join the thread back to the main thread
    # we can run any number of threads
    for i in range(0,10):
        thread = threading.Thread(target=executeThread, args=(i,)) # we pass in args as a tuple
        # thread = threading.Thread(target=executeThread, args={'i':i}) # we pass in args as a dict
        thread.start()
        print('Active threads: {}'.format(threading.enumerate()))
        # thread.join() # how can we join our threads and remain concurrent?