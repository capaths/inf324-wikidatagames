"""Access Service"""

import requests
import json

from nameko.rpc import rpc, RpcProxy
from nameko.exceptions import RemoteError
import jwt

import time
import json

from secret import JWT_SECRET


class NotAuthenticated(Exception):
    pass


class AccessService:
    name = 'access'

    player_rpc = RpcProxy("player")
    auth = RpcProxy("access")

    @rpc
    def login(self, username, password):

        try:
            player = self.player_rpc.get_player(username, password)
        except RemoteError:
            raise NotAuthenticated()

        token = jwt.encode({
            'username': player["username"],
            "exp": time.time() + 60
        }, JWT_SECRET, algorithm='HS256')
        return json.dumps({"jwt": token.decode(), "user": player})

    @rpc
    def signup(self, username, password):

        data = {
            "username": username,
            "password": password,
            "country": "Chile",
            "elo": 1000
        }

        req = requests.post("http://player:8080/player", json=data)

        if req.status_code == 400:
            raise ValueError("Invalid player field values")
        elif req.status_code != 200:
            raise RemoteError(req.content)
