# we have a finite number of tickets available, distributed between ticket agents
# the semaphore can control who gets to sell the next ticket
import random
import sys
from time import time
import threading

class TicketSeller(threading.Thread):
    ticketsSold = 0
    def __init__(self, sem): # we can pass n a semaphore to be shared by all instances of this class
        threading.Thread.__init__()
        self.__sem = sem
        sys.stdout.write('Ticket seller has started selling tickets')
    def run(self):
        global ticketsAvailable
        running = True # a flag
        while running:
            self.randomDelay()
            self.__sem.acquire() # acquire the semaphore that is shared across all isntances
            if ticketsAvailable <=0:
                running = False
            else:
                self.ticketsSold += 1
                ticketsAvailable -= 1
                sys.stdout.write('{} sold a ticket. There are {} tickets remaining\n'.format(self.getName(), ticketsAvailable))
            self.__sem.release()
        # when all done...
        sys.stdout.write('Ticket seller {} sold {} tickets\n'.format(self.getName(), self.ticketsSold))

    def randomDelay(self):
        time.sleep(random.randint(0,4)/4) # 0, 0.25, 0.5 or 0.75 seconds

if __name__ == '__main__':
    ticketsAvailable = 1000 # how many tickets to sell
    # we need a semaphore
    sem = threading.Semaphore(2) # how many concurrent shares of this semaphore
    sellers = []
    for i in range(4):
        seller = TicketSeller(sem) # they all share the same semaphore
        sellers.append(seller)
        seller.start()
    # once all threads are started, we can join them
    for seller in sellers:
        seller.join()
