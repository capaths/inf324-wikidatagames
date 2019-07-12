"""Access Service"""

from flask import Flask

APP = Flask(__name__)


@APP.route("/")
def index():
    """Home route"""
    return "<h1>Access Service</h1>"


if __name__ == "__main__":
    APP.run(host="0.0.0.0")
