#!/usr/bin/python
"""import flask"""

from flask import Flask, render_template

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

#
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

""" Define a route for '/number_template/<n>'"""
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number_template.html', n=n)
    

#
""" Define a route for '/number_odd_or_even/<n>'"""
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)