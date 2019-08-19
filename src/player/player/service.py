"""Player Service"""
from nameko.web.handlers import http
from nameko.rpc import rpc
from player.models import Player, PlayerDatabase
from player.schemas import PlayerSchema
from nameko.exceptions import BadRequest


class PlayerService:
    name = "player"

    rep = PlayerDatabase()

    @http('POST', '/player')
    def create_player(self, request):
        schema = PlayerSchema(strict=True)
        try:
            player_data = schema.loads(request.get_data(as_text=True)).data
        except ValueError as exc:
            raise BadRequest("Invalid json: {}".format(exc))

        username = player_data['username']
        password = player_data['password']
        country = player_data['country']
        elo = player_data['elo']

        try:
            player = Player(username=username, password=password, country=country, elo=elo, jwt=None)
        except AssertionError:
            return 400, "Player not valid"

        self.rep.db.add(player)
        self.rep.db.commit()

        return 200, "Ok"

    @rpc
    def get_player_by_username(self, usernm):
        player = self.rep.db.query(Player).filter(Player.username == usernm).first()
        if not player:
            return None
        return PlayerSchema().dump(player).data

    @rpc
    def get_player(self, usernm, passw):
        player = self.rep.db.query(Player).filter(Player.username == usernm).first()
        if not player:
            raise ValueError('Player {} no encontrado'.format(usernm))
        if player.password != passw:
            raise ValueError(f'Contrasenna mal ingresada')

        return PlayerSchema().dump(player).data
