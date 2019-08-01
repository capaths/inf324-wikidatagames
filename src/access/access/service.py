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


    @rpc
    def login(self, username, password):

        try:
            player = self.player_rpc.get_player(username, password)
        except RemoteError:
            raise NotAuthenticated()

        token = jwt.encode({
            'username': player["username"],
            'permissions': [],
            'roles': [],
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

        req = requests.post("http://player:8888/player", json=data)

        if req.status_code == 200:
            return 200, self.login(username, password)
        else:
            return req.status_code, req.content
