""" Gateway """

from nameko.rpc import RpcProxy
from nameko.web.handlers import http
from nameko.exceptions import BadRequest, RemoteError

from schemas import LoginSchema

import json


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
    def login(self, request):
        schema = LoginSchema(strict=True)

        try:
            login_data = schema.loads(request.get_data(as_text=True)).data
        except ValueError as exc:
            raise BadRequest("Invalid json: {}".format(exc))

        username = login_data["username"]
        password = login_data["password"]

        try:
            user_data = self.auth.login(username, password)
        except RemoteError:
            return 400, "Invalid Credentials"

        return str(user_data)

    @http("POST", "/signup")
    def signup(self, request):
        schema = LoginSchema(strict=True)

        try:
            login_data = schema.loads(request.get_data(as_text=True)).data
        except ValueError as exc:
            raise BadRequest("Invalid json: {}".format(exc))

        username = login_data["username"]
        password = login_data["password"]

        try:
            self.auth.signup(username, password)
        except RemoteError as exc:
            return 500, exc.value

        return 200, "Successful sign-up"
