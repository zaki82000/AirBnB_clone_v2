#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ displays a cities_by_states.html page """
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def taredown(exeption):
    """ taredown """
    storage.close()


if __name__ == '__main__':
    app.run()
