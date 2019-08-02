import os

from flask import Flask, render_template
from flask import request

import requests

app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist")


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    country = data["country"]

    req = requests.post("http://gateway:8000/signup", json={
        "username": username,
        "password": password,
        "country": country
    })

    return req.content.decode()


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]

    if os.environ.get("ENV") != "prod":
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

    if os.environ.get("ENV") == "prod":
        req = requests.post("http://gateway:8000/logout", json={
            "jwt": jwt,
        })

    return "", 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
