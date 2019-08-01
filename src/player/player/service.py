"""Player Service"""


import json
from nameko.web.handlers import http
from nameko.events import EventDispatcher
from nameko.rpc import rpc
from nameko_sqlalchemy import DatabaseSession
from player.models import DeclarativeBase, Player
from player.schemas import PlayerSchema
from nameko.exceptions import BadRequest


class PlayerService:
    name = "player"

    db = DatabaseSession(DeclarativeBase)
    #event_dispatcher = EventDispatcher()

    @http('POST','/player')
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
        player = Player(username=username, password=password, country=country, elo=elo)
        self.db.add(player)
        self.db.commit()



        #self.event_dispatcher('order_created', {
        #    'order': order,
        #})

        return str(player)