from memory_profiler import profile # may need to pip isntall memory_profiler
import collections

@profile # we can decorate ANY function to get a memory profile
def someFn():
    # here is a double-ended queue
    my_deq = collections.deque('98765432')
    # we can alter members of the queue
    my_deq.append('1')
    my_deq.appendleft('0')
    my_deq.pop() # remove from the right
    my_deq.popleft() # remove from the left
    print(my_deq)


if __name__ == '__main__':
    someFn()