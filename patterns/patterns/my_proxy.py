# a proxy example is nft (non-fungible tokens)
# here we will implement a bank with several payment methods (proxies)

import random
from abc import ABC, ABCMeta, abstractmethod

class Payment(metaclass = ABCMeta):
    @abstractmethod
    def do_pay(self):
        pass

class Bank(Payment):
    def __init__(self):
        self.card = None
        self.account = None
    def setCard(self, card):
        self.card = card
    def __getAccount(self):
        self.account = self.card
        return self.account
    def __has_funds(self):
        print('Bank is checking if {} has sufficient funds'.format( self.__getAccount() ))
        # randomly decide if there are funds
        return bool(random.getrandbits(1)) # performant way to return True or False randomly
    def do_pay(self):
        if self.__has_funds():
            print('bank is paying')
            return True
        else:
            print('insufficient funds')
            return False

class DebitCard(Payment):
    def __init__(self):
        self.bank = Bank() # now our debit card is a proxy for the bank
    def do_pay(self):
        card = input('Swipe, Tap or Insert card? ')
        self.bank.setCard(card)
        # call the do_pay method of the bank (for which we are a proxy)
        return self.bank.do_pay()

class You(): # this will be the client of the proxy
    def __init__(self):
        print('Lets buy some stuff...')
        self.debitCard = DebitCard() # we instantiate our proxy
        self.isPurchased = None
    def makePayment(self):
        self.isPurchased = self.debitCard.do_pay() # use our proxy
    def __del__(self):
        if self.isPurchased:
            print('we bought something!')
        else:
            print('lend me a fiver?')

if __name__ == '__main__':
    you  =You() # here is an instance of the client
    you.makePayment() # try to use our proxy