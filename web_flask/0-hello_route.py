#!/usr/bin/python3
from flask import Flask

HBNB_app = Flask(__name__)

@HBNB_app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB!"

if __name__ == "__main__":
    HBNB_app.run(debug=True, host='0.0.0.0', port= 5000)
