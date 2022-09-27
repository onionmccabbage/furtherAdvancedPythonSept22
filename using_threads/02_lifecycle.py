# threads can be defined by functions or by classes
import threading
import time
# each thread has a life cycle
def threadWorker(): # this function is callable to run in as many threads as we like
    print('thread is running')
    time.sleep(2)
    print('thread is terminating')

if __name__ == '__main__':
    myThread = threading.Thread(target=threadWorker)
    myThread.start() # the function will execute on its own separate thread
    myThread.join() # best practice to join the thread back to the main thread