# here we explore conventional coroutines
from asyncio import coroutines, events

# In Python, generators are coroutines = they can yield more than one value
even_g = (i for i in range(1,10) if i%2 == 0)
print(type(even_g)) # it's a generator
print(even_g.__next__()) # 2
print(even_g.__next__()) # 4
for member in even_g:
    print(member) # 6, 8

# we can write a custom coroutine (a custom generator)
def tally(inc): # normal function s have a 'return'. coroutines/generators have 'yield'
    score = 0
    while True:
        yield score
        score += inc

if __name__ == '__main__':
    w = tally(5)    # tally is a function 
    print(type(w)) # ...but w is a generator
    print(next(w))
    print(next(w))
    print(next(w))
    print(next(w))
    print(next(w))
    print(w.__next__())
    # another generator...
    b = tally(3)
    print(next(b)) #0
    print(next(b)) #3

    print(w.send(7))
    print(next(w))

    # tidy up
    w.close()
    b.close()
