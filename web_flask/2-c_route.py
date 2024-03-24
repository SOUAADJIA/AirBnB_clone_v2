#!/usr/bin/python3
"""
Starts a Flask web application.

The web application listens on 0.0.0.0, port 5000.
Routes:
    /: display "Hello HBNB!"
    /hbnb: display "HBNB"
    /c/<text>: display "C " followed by the value of the text variable
               (replace underscore _ symbols with a space)
You must use the option strict_slashes=False in your route definition
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Displays 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Displays 'C' followed by the value of the text variable"""
    text_fix = f'{text}'.replace('_', ' ')
    return f'C {text_fix}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
