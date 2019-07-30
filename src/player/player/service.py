"""Player Service"""

from nameko.rpc import rpc
import json


class PlayerService:
    name = "player"

    @rpc
    def create_player(self, username, password, country):
        pass

    @rpc
    def get_player(self, username):
        return json.dumps({"username": "user", "country": "Chile"})
