#!/usr/bin/python3
"""
This module implements a Flask web application with
various routes for displaying messages.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """
    Display a greeting message.
    :return: A string containing the greeting message.
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Display "HBNB".
    :return: A string containing the message "HBNB".
    """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Display "C ", followed by the value of the text variable.
    Underscore "_" symbols are replaced with spaces.
    :param text: The value to be displayed after "C ".
    :return: A string containing the modified message.
    """
    return f'C {text.replace("_", " ")}'

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Display "Python ", followed by the value of the text variable.
    Underscore "_" symbols are replaced with spaces.
    The default value of text is "is cool".
    :param text: The value to be displayed after "Python ".
    :return: A string containing the modified message.
    """
    return f'Python {text.replace("_", " ")}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)