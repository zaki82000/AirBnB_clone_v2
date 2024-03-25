#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """ display a 10-hbnb_filters.html page """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


@app.teardown_appcontext
def taredown(exeption):
    """ taredown """
    storage.close()


if __name__ == '__main__':
    app.run()
