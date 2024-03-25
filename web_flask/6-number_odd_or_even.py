#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask, render_template

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


@app.route('/number/<int:number>', strict_slashes=False)
def its_a_number(number):
    """ displays 'n is a number' only if n is an integer """
    return f'{number} is a number'


@app.route('/number_template/<int:number>', strict_slashes=False)
def number_template(number):
    """ displays a HTML page only if n is an integer """
    return render_template('5-number.html', number=number)


@app.route('/number_odd_or_even/<int:number>', strict_slashes=False)
def number_odd_or_even(number):
    """
    displays a HTML page only if n is an integer
    with H1 tag: 'Number: n is even|odd' inside the tag BODY
    """
    return render_template('6-number_odd_or_even.html', number=number)


if __name__ == '__main__':
    app.run()
