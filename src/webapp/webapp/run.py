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
    username = request.values["username"]
    password = request.values["password"]
    country = "Chile"

    req = requests.post("http://gateway:8000/signup", json={
        "username": username,
        "password": password,
        "country": country
    })

    return req.content.decode()


@app.route('/login', methods=['POST'])
def login():
    username = request.values["username"]
    password = request.values["password"]

    req = requests.post("http://gateway:8000/login", json={
        "username": username,
        "password": password
    })

    return req.content.decode()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
