# here we make use of the Reactive extensions for Python (RxPY)
from util import filterNames
import requests # may need to pip isntall requests
# may need to pip install rx
import rx
# we can choose which operators to use from the rx library
from rx import operators as op # there are tons of really useful operators

def main():
    # ask the user which letter to match
    letter = input('starts with...? ')
    # fetch all the users from the API end-point
    content = requests.get('https://jsonplaceholder.typicode.com/users')
    # convert the returned JSON to Python list of dictionaries
    y = content.json()
    # we need an observable
    source_obs = rx.from_(y) # could use from_list
    # we make use of our observable
    case1 = source_obs.pipe( # this will async await for the data to be ready
        # these operations only operate when the data is ready
        op.filter( lambda c:filterNames(c, letter) ),
        op.map( lambda a:a['name'] ) # or any part of our data
    )
    # we can subscribe as many times as we like...
    case1.subscribe(
        # we can implement next, error and complete handlers
        on_next      = lambda i:print('Received {}'.format(i)),
        on_error     = lambda e: print('Received Error {}'.format(e)),
        on_completed = lambda: print('All done')
    )

if __name__ == '__main__':
    main()
