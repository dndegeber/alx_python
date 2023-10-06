#!/usr/bin/python3
"""
This module is a simple Flask application that
greets users when they access the root URL.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """
    Function to handle requests to the root URL ('/')
    and return a greeting message.
    :return: A string containing the greeting message.
    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

