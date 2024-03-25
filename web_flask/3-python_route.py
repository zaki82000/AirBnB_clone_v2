#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ displays 'Hello HBNB!' """
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ displays 'HBNB' """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """  displays 'C' followed by the value of the text variable """
    return f'C {text.replace("_", " ")}'


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is_cool'):
    """
    displays 'Python' followed by the value of the text variable
    with default value of text is 'is cool'
    """
    return f'Python {text.replace("_", " ")}'


if __name__ == '__main__':
    app.run()
