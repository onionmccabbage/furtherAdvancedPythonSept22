import asyncio

# we would make a function 'async' if there is a chance it might take a while
# e.g. data access from db, file, sensor, API...
async def square(number):
    return number*number

async def main():
    x = await square(10)
    print(x)
    y = await square(5)
    print(y)

if __name__ == '__main__':
    # in the modern context, a coroutine is 
    # conventionally invoked like this
    asyncio.run( main() )