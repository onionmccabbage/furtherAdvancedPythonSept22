# using the command design pattern
from abc import ABCMeta, abstractmethod

class Order(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass
# here are some concrete classes
class StockTrade():
    def buy(self):
        print('buy stocks')
    def sell(self):
        print('sell stocks')

class Agent():
    def __init__(self):
        self.__orderQueue = [] # start with an empty list of things to do
    def placeOrder(self, order):
        self.__orderQueue.append(order)
        order.execute() # we may need to wait until resourcces become available

class BuyStock(Order): # inherit from the Order abstract base class
    def __init__(self, stock):
        self.stock = stock
    def execute(self):
        return self.stock.buy()

class SellStock(Order): # inherit from the Order abstract base class
    def __init__(self, stock):
        self.stock = stock
    def execute(self):
        return self.stock.sell()

if __name__ == '__main__':
    # exercise the code
    stock = StockTrade()
    buy   = BuyStock(stock)
    sell  = SellStock(stock)

    # invoke the commands
    agent = Agent() # the agent will cary out the commands, in this case using a queue
    agent.placeOrder(buy)
    agent.placeOrder(sell)
