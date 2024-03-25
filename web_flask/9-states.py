#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """ display a states.html page """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_by_id(id):
    """ display a states.html page """
    if id:
        try:
            state = storage.all(State)[f'State.{id}']
            return render_template('9-states.html', state=state)
        except KeyError:
            return render_template('9-states.html')


@app.teardown_appcontext
def taredown(exeption):
    """ taredown """
    storage.close()


if __name__ == '__main__':
    app.run()
