"""Player Service"""
import json
from nameko.web.handlers import http
from nameko.events import EventDispatcher
from nameko.rpc import rpc
from nameko_sqlalchemy import DatabaseSession
from ticket.models import DeclarativeBase, Player
from ticket.schemas import TicketSchema
from nameko.exceptions import BadRequest

class TicketService:
    name = "ticket"
    db = DatabaseSession(DeclarativeBase)

    @http('POST','/ticket')
    def create_ticket(self, request):
        schema = TicketSchema(strict=True)
        try:
            ticket_data = schema.loads(request.get_data(as_text=True)).data
        except ValueError as exc:
            raise BadRequest("Invalid json: {}".format(exc))

        title = ticket_data['title']
        description = ticket_data['description']

        ticket = Ticket(title=title,description=description)
        self.db.add(ticket)
        self.db.commit()

        #self.event_dispatcher('order_created', {
        #    'order': order,
        #})


        return 200

    @rpc
    def get_all_tickets(self):
    	ticket = self.db.query(Ticket).order_by(Ticket.id)
    	array = []
        for instance in ticket:
        	dicto = {}
        	dicto['id'] = instance.id
        	dicto['title'] = instance.title
        	dicto['description'] = instance.description
        	array.append(dicto)
		return json.dumps(array)

	@rpc
	def get_ticket(self, id)
		ticket = self.db.query(Ticket).filter(Ticket.id = id).first()
		if not ticket:
            raise NotFound('Ticket {} no encontrado'.format(id))
        return TicketSchema().dump(ticket).data


