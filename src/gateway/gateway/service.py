""" Gateway """

from nameko.rpc import RpcProxy
from nameko.web.handlers import http
from nameko.exceptions import BadRequest

from schemas import LoginSchema


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

        jwt = self.auth.login(username, password)
        return jwt

    @http("POST", "/signup")
    def signup(self, request):
        schema = LoginSchema(strict=True)

        try:
            login_data = schema.loads(request.get_data(as_text=True)).data
        except ValueError as exc:
            raise BadRequest("Invalid json: {}".format(exc))

        username = login_data["username"]
        password = login_data["password"]

        jwt = self.auth.signup(username, password)
        return jwt
