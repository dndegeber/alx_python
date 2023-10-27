#!/usr/bin/python
"""
import flask and request from the imported flask
"""


from flask import Flask
from flask import request

app = Flask(__name__)

""" Define a route for the root URL '/'"""
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

""" Define a route for '/hbnb'"""
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

""" Define a route for '/c/<text>'"""
@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """ Replace underscores with spaces in the text"""
    text_with_spaces = text.replace('_', ' ')
    return 'C {}'.format(text_with_spaces)

""" Define a route for '/python/<text>'"""
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is cool"):
    """ Replace underscores with spaces in the text"""
    text_with_spaces = text.replace('_', ' ')
    return 'Python {}'.format(text_with_spaces)

""" Define a route for '/number/<n>'"""
@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    return '{} is a number'.format(n)

if __name__ == '__main__':
    """ Run the Flask app on 0.0.0.0 and port 5000"""
    app.run(host='0.0.0.0', port=5000)