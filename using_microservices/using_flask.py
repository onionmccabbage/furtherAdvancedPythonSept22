# flask implements many of the things we need from microservices
# NB use Django for full-fat web capabilities

from flask import Flask # may need to pip install flask
from flask import render_template 

from memory_profiler import profile # we could profile our code...

# NB any changes will only be seen when the server is re-started

# we begin by declaring a flask app
app = Flask(__name__) # by convention use the __name__ that Python assigns
# declare the root path (and other routes)
@app.route('/') # the root of our application
def root():
    # anything can be passed - plain text, json, html etc.
    # we can declare an HTML response
    content = ''' 
    <h1>we are at the root of this service</h1>
    <a href='/hello'>greeting</a>
    '''
    return content
@app.route('/hello') # not /hello/ !!!
@app.route('/hello/<name>') # many routes can use the SAME function
def hello(name=None):
    # if name != None:
    #     return render_template('greeting.html') # Flask will look for a package called 'templates'
    #     # return '''
    #     # Greetings {} welcome to Flask
    #     # '''.format(name)
    # else:
    #     return '<h2>Hello from Flask</h2>'
    return render_template('greeting.html', name=name)

def main():
    app.run(host='127.0.0.1') # localhost

if __name__ == '__main__':
    main()