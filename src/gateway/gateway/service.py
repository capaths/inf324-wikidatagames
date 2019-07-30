""" Gateway """

import json

from nameko.rpc import RpcProxy
from nameko.web.handlers import http


class GatewayService:
    """
    Gateway for other services
    """

    name = "gateway"

    auth = RpcProxy('access')

    ticket_rpc = RpcProxy('ticket')
    chat_rpc = RpcProxy('chat')
    match_rpc = RpcProxy('match')
    player_rpc = RpcProxy('player')

    @http("GET", "/player")
    def get_player(self, request):
        return self.player_rpc.get_player("user")

    @http("POST", "/login")
    def login(self, username, password):
        return self.access_rpc.login(username, password)

    @http("POST", "/signup")
    def signup(self, username, password, country):
        return self.access_rpc.signup(username, password, country)
