#!/usr/bin/python3
"""
This module implements a simple Flask application.
"""

from flask import Flask

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


@hbnb_app.route("/python/<text>", strict_slashes=False)
def display_python(text):
    """
    This function handles requests to the '/python/<text>' URL.
    It returns "python " followed by the value of the text variable
    with underscores replaced by spaces.
    """
    return "Python " + text.replace("_", " ")


if __name__ == "__main__":
    hbnb_app.run(debug=True, host='0.0.0.0', port=5000)
