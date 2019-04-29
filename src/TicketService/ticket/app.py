"""Ticket Service"""

from flask import Flask

APP = Flask(__name__)


@APP.route("/")
def index():
    """Home route"""
    return "<h1>Ticket Service</h1>"
