import multiprocessing

# unlike multithreading, each process has its OWN copy of Python
# Therefore there is NO global interpreter lock degredation

def myProcFn():
    print('Process in a separate copy of Python')

if __name__ == '__main__':
    print('in te main process')
    # each process starts in a separate CPU
    myOtherProcA = multiprocessing.Process(target=myProcFn)
    myOtherProcB = multiprocessing.Process(target=myProcFn)
    myOtherProcC = multiprocessing.Process(target=myProcFn)
    myOtherProcA.start()
    myOtherProcB.start()
    myOtherProcC.start()
    myOtherProcA.join()
    myOtherProcB.join()
    myOtherProcC.join()
    print('all done')