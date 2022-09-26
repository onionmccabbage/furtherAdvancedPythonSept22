# A decorator adds something to what we already have
# here is a function which will be used to decorate other functions
def showArgs(f): # this decorator takes a function as an argument. Then reveal the positional and keyword arguments
    def new_func(*args, **kwargs):
        # *args is the tuple of any passed-in positional armuments
        # **kwargs is the dictionary of any pased-in keyword arguments
        print('Running a function called {}'.format(f.__name__))
        print('Positional arguments are {}'.format(args)) # tuple
        print('Keyword arguments are {}'.format(kwargs)) # dictonary
        return f(*args, **kwargs) # run the actual function with the original arguments
    return new_func 

@showArgs # apply our decorator to ANY other function
def addIntegers(a, b):
    return a+b

@showArgs
def raiseToPower(m, n):
    return m**n

if __name__ == '__main__':
    print( addIntegers(1,2) ) # here we pass in positional arguments. They will end up in the tuple called *args
    print( addIntegers(a=1, b=2) ) # here we pass in keyword arguments. They will end up in the **kwargs dictionary
    print( addIntegers(1, b=2) ) # here we pass in keyword and positional arguments


