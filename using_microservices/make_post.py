# there are a number of HTTP verbs
# the most common by far is 'get' which is limited, (typically 2048 characters)
# we also have 'post' which has no limit on the size of the data sent (data is ssnt separately to the request header)
# also 'put', 'update' and 'delete'

# to make a post send the data as a payload
# from urllib import request # historically Python used hte urllib to assemble requersts
# but these days we use the 'requests' library
import requests

def makePost():
    url = 'http://httpbin.org/post' # this is a convenient demo server
    payload = {'item':'bottle', 'price':'123'}
    try:
        r = requests.post(url, payload)
        print(r.text) # lets see the response
    except Exception as err:
        print(err)

if __name__ == '__main__':
    makePost()

