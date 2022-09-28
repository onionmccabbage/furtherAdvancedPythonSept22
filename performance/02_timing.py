from re import L
from time import sleep, time
import random
import time
import timeit # timeit is aware of system time and process/thread time and can leave out system-related time

def timeThis(func): # this will be a decorator for other function
    def function_timer(*args, **kwargs):
        start_time = timeit.default_timer() # timeit is more accurate than just 'time.time'
        value = func(*args, **kwargs)
        run_time= timeit.default_timer() - start_time # calculate how long the func tok to run
        print('{} took {} seconds'.format(func.__name__, run_time))
    return function_timer

@timeThis # use our function to decorate any function we wish to time
def long_runner():
    for x in range(9):
        sleep_for  = random.choice(range(1,3)) # sleep for one or two seconds
        time.sleep(sleep_for)

# q - is there a difference in counting upwards or downwards?
@timeThis # there is no statistical difference
def count_up():
    for i in range(0,10):
        x = i
@timeThis
def count_down():
    for i in range(9, -1, -1):
        x = i

if __name__ == '__main__':
    # long_runner()
    count_up()
    count_down()
    #
    count_down()
    count_up()