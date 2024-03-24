#!/usr/bin/python3
"""
This module implements a simple Flask application.
"""

from flask import Flask, render_template

hbnb_app = Flask(__name__)


@hbnb_app.route("/", strict_slashes=False)
def index():
    """
    This function handles requests to the root URL.
    It returns a simple greeting message.
    """
    return "Hello HBNB!"


@hbnb_app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    This function handles requests to the '/hbnb' URL.
    It returns a message indicating 'HBNB'.
    """
    return "HBNB"


@hbnb_app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    """
    This function handles requests to the '/c/<text>' URL.
    It returns "C " followed by the value of the text variable
    with underscores replaced by spaces.
    """
    return "C " + text.replace("_", " ")


@hbnb_app.route("/python/", defaults={'text': "is cool"}, strict_slashes=False)
@hbnb_app.route("/python/<text>", strict_slashes=False)
def display_python(text):
    """
    This function handles requests to the '/python/<text>' URL.
    It returns "Python " followed by the value of the text variable
    with underscores replaced by spaces. The default value of text is "is cool"
    """
    return "Python " + text.replace("_", " ")


@hbnb_app.route("/number/<int:n>", strict_slashes=False)
def display_number(n):
    """
    This function handles requests to the'/number/<n>'URL where <n> is a number
    It returns a message indicating that <n> is a number.
    """
    return f"{n} is a number"


@hbnb_app.route("/number_template/<int:n>", strict_slashes=False)
def display_html(n):
    """
    This function handles requests to the '/number_template/<n>' URL.
    It checks if the provided value <n> is an integer.
    If <n> is an integer, it renders an
    HTML template named 'number_template.html'.
    The template contains an H1 tag with the text
    "Number: n", where 'n' is the provided integer.
    """
    return render_template("5-number.html", n=n)


@hbnb_app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def display_html(n):
    """
    This function handles requests to the '/number_odd_or_even/<n>' URL.
    It checks if the provided value <n> is an integer.
    If <n> is an integer, it renders an HTML page.
    The HTML page contains an H1 tag displaying whether the provided
    number <n> is even or odd.
    """
    if isinstance(n, int):
        return render_template("number_odd_or_even.html", n=n)


if __name__ == "__main__":
    hbnb_app.run(debug=True, host='0.0.0.0', port=5000)
