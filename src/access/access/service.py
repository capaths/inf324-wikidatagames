"""Access Service"""

import requests

from nameko.rpc import rpc
import jwt

from secret import JWT_SECRET


class NotAuthenticated(Exception):
    pass


class AccessService:
    name = 'access'

    @rpc
    def login(self, username, password):
        if password == "secret":
            token = jwt.encode({
                'username': username,
                'permissions': [],
                'roles': []
            }, JWT_SECRET)
            return token.decode()
        raise NotAuthenticated()

    @rpc
    def signup(self, username, password):

        data = {
            "username": username,
            "password": password,
            "country": "Chile",
            "elo": 1000
        }
        req = requests.post("http://player:8888/player", json=data)

        if req.status_code == 200:
            return self.login(username, password)
        else:
            return req.status_code, req.content
