#!/usr/bin/python3
"""
Script that starts a Flask web application_task 10
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """Display a HTML page with a list of all State objects"""
    states = sorted(storage.all("State").values(), key=lambda x: x.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_cities_list(id):
    """Display a HTML page with a list of City objects linked to a State"""
    state = storage.get("State", id)
    if state:
        return render_template('9-states.html', state=state)
    return render_template('9-states.html', state=None)


@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
