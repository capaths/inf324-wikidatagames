import os

from flask import Flask, render_template
from flask import request

from flask_webpack_loader import WebpackLoader
import re
import sys

import requests


def create_app(for_production):
    template_folder = "../dist" if for_production else "./templates"
    static_folder = "../dist/static" if for_production else "static"

    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)

    if not PROD:
        WEBPACK_LOADER = {
            'BUNDLE_DIR_NAME': os.path.join('static', 'bundles'),
            'STATIC_URL': 'static',
            'STATS_FILE': './frontend/webpack-stats.json',
            'POLL_INTERVAL': 0.1,
            'TIMEOUT': None,
            'IGNORES': [re.compile(r'.+\.hot-update.js'), re.compile(r'.+\.map')],
            'CACHE': False
        }

        webpack_loader = WebpackLoader(app)
        webpack_loader.config = WEBPACK_LOADER

    return app


PROD = os.environ.get("ENV") == "prod"
app = create_app(PROD)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    country = data["country"]

    if PROD:
        req = requests.post("http://gateway:8000/signup", json={
            "username": username,
            "password": password,
            "country": country
        })

        if req.status_code != 200:
            return req.content.decode(), req.status_code
    return login()


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]

    if not PROD:
        user = {
            "jwt": "test-jwt",
            "user": {
                "username": "testUser",
                "country": "Chile"
            }
        }
        status_code = 200
    else:
        req = requests.post("http://gateway:8000/login", json={
            "username": username,
            "password": password
        })
        user = req.content.decode()
        status_code = req.status_code

    return user, status_code


@app.route('/logout', methods=['POST'])
def logout():
    data = request.get_json()
    jwt = data["jwt"]

    if PROD:
        req = requests.post("http://gateway:8000/logout", json={
            "jwt": jwt,
        })

    return "", 200
