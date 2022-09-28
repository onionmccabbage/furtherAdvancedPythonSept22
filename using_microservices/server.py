import sys
import socket # a socket server for listening to http(s) requests

def myServer():
    # we configure our server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    params_t = ('localhost', 9874)
    server.bind(params_t)
    # begin listening for requests
    server.listen(6) # how many concurrent client request can we handle
    print('Server is listening on {} port {}'.format(params_t[0], params_t[1]))
    # run the server continously
    while True: # careful...
        # unpack the request
        (client, addr) = server.accept()
        # read any data from the client
        buf = client.recv(1024) # here we read the first 1024 bytes received
        print('Server received {}'.format(buf))
        # send a response back to the client
        client.send(buf.upper()) # echo back an uppercase version
        # we need a way to quit the server
        if buf == b'quit':
            print('server is closing')
            server.close()
            break # this will stop the while loop

if __name__ == '__main__':
    myServer() # start our server