import multiprocessing
import os
from typing_extensions import Self # a library to access the operating system

# remember - this is a Process ACCESS object, not the process itself
class MyProcess(multiprocessing.Process):
    def __init__(self):
        super(MyProcess, self).__init__()
    # override the default run method
    def run(self):
        print('Child process ID is {}'.format(multiprocessing.current_process().pid))

def main():
    processes = []
    for i in range(os.cpu_count()-1 ): # no point having more processes than cores
        p = MyProcess()
        processes.append(p)
        p.start()
    for proc in processes:
        proc.join() # good practice

if __name__ == '__main__':
    print('Main process ID is {}'.format(multiprocessing.current_process().pid))
    main()

