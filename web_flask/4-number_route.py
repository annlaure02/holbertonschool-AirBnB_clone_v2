#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """ display “Hello HBNB!” """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ display “HBNB” """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """
    display “C ” followed by the value of the text variable
    and replace underscore with a space
    """
    text = text.replace("_", " ")
    return f"C {escape(text)}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>")
def python_text(text="is cool"):
    """
    display “Python ”, followed by the value of the text variable
    and replace underscore with a space
    """
    text = text.replace("_", " ")
    return "Python %s" % text


@app.route("/number/<int:n>", strict_slashes=False)
def number_n(n):
    return "%d is a number" % n


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
