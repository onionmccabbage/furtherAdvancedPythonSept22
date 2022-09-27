from threading import Thread
import time

def standardThread():
    print('starting a standard thread')
    time.sleep(20)
    print('end the standard thread')

def daemonThread():
    while True: # CAREFUL - this is an endless loop!!!
        print('heartbeat...')
        time.sleep(2)

if __name__ == '__main__':
    s = Thread(target=standardThread)
    d = Thread(target=daemonThread)
    d.setDaemon(True) # we now have a daemon thread
    s.start()
    d.start() # no 'join' for daemon threads
    s.join()