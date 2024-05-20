#!/usr/bin/python3
"""Starts a flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """
    Display Hello HBNB
    """
    return 'Hello HBND'


if __name__ == "__main__":
    app.run()
