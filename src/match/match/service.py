"""Match Service"""

from nameko.rpc import rpc
from nameko.extensions import DependencyProvider
from nameko.web.websocket import WebSocketHubProvider, rpc

import json
from nameko.web.handlers import http
from nameko.events import EventDispatcher
from nameko.rpc import rpc
from nameko_sqlalchemy import DatabaseSession
from match.models import DeclarativeBase, Player
from match.schemas import MatchSchema
from nameko.exceptions import BadRequest


# class ContainerIdentifier(DependencyProvider):
#    def get_dependency(self, worker_ctx):
#        return id(self.container)

class MatchService:
    name = "match"
    db = DatabaseSession(DeclarativeBase)

    @http('POST', '/match')
    def create_match(self, request):
        schema = TicketSchema(strict=True)
        try:
            match_data = schema.loads(request.get_data(as_text=True)).data
        except ValueError as exc:
            raise BadRequest("Invalid json: {}".format(exc))

        idPlayer1 = match_data['idPlayer2']
        idPlayer2 = match_data['idPlayer1']
        scorePlayer1 = match_data['scorePlayer1']
        scorePlayer2 = match_data['scorePlayer2']
        result = match_data['result']

        match = Match(idPlayer1=idPlayer1, idPlayer2=idPlayer2, scorePlayer1=scorePlayer1, scorePlayer1=scorePlayer2,
                      result=result)
        self.db.add(match)
        self.db.commit()

        # self.event_dispatcher('order_created', {
        #    'order': order,
        # })

        return 200

    @http('GET','/flag')
    def get_flag(self, request):
        file1 = open('images.txt', 'r')
        sample_list = random.sample(range(0, 70), 20)

        name, url = [], []
        for i in file1:
            splitter = i.split(';')
            if int(splitter[0]) in sample_list:
                name.append(splitter[2])
                url.append(splitter[3])

        data = [{"name": t, "image_url": s} for t, s in zip(name, url)]
        return json.dumps(data)

    @rpc
    def get_all_match(self):
        match = self.db.query(Match).order_by(Match.id)
        array = []
        for instance in match:
            dicto = {}
            dicto['id'] = instance.id
            dicto['idPlayer1'] = instance.idPlayer1
            dicto['idPlayer2'] = instance.idPlayer2
            dicto['scorePlayer1'] = instance.scorePlayer1match
            dicto['scorePlayer2'] = instance.scorePlmatch
            dicto['result'] = instance.result
            array.append(dicto)
            return json.dumps(array)

        @rpc
        def get_match(self, id)
            match = self.db.query(Match).filter(Match.id = id).first()
            if not match:
            raise NotFound('Match {} no encontrado'.format(id))
        return MatchSchema().dump(match).data
