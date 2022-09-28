# modern Python has a 'green' event called gevent
# gevent can run threads on our behalf
import gevent
from gevent import socket

# here we will access a list of URLs and retrieve data in a thread safe way
hosts = ['www.ericsson.com', 'www.neueda.com', 'www.crappytaxidermy.com', 'jsonplaceholder.typicode.com', 'bbc.co.uk']
# set up some jobs to be carried out
jobs = [ gevent.spawn(socket.gethostbyname, host) for host in hosts ]

# start all the threds then join them
gevent.joinall(jobs, timeout=5)
for job in jobs:
    print(job.value)
