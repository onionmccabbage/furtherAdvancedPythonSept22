from threading import Thread # NB 'Thread' is a thread-access object

# NB we can tell Python to optimize for threads like this:
# python module.py -o
# without -o Python will make no thread-optimizations

class MyWorkerThread(Thread):
    def __init__(self):
        print('instance of MyWorkerThread class')
        Thread.__init__(self)
    # we override the default 'run' method of Thread
    def run(self):
        print('thread is running') # here we write the businesss logic for this thread

if __name__ == '__main__':
    myThread = MyWorkerThread() # create an instance of our Thread class
    myThread.start()
    myThread.join()