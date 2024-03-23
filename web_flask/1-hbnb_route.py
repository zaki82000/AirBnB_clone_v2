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


if __name__ == "__main__":
    hbnb_app.run(debug=True, host='0.0.0.0', port=5000)
