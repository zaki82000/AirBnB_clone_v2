#!/usr/bin/python3
from flask import Flask

hbnb_app = Flask(__name__)


@hbnb_app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB!"


if __name__ == "__main__":
    hbnb_app.run(debug=True, host='0.0.0.0', port=5000)
