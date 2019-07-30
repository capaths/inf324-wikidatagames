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
    def get_player(self, req):
        return self.player_rpc.get_player("user")
