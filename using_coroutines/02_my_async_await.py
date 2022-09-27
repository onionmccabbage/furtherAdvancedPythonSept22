# modern Python lets us manage asynchronous code using 'async' and 'await'
import asyncio
# here is a normal function, set as 'async'
# if we use async we MUST use await (or similar)
async def square(number): # async makes this a coroutine
    return number*number

if __name__ == '__main__':
    # here 'run' implicitly awaits the result
    result = asyncio.run(square(3))
    print( result ) # 9