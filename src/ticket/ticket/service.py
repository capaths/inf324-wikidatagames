"""Ticket Service"""
from __future__ import absolute_import

import json
from nameko.web.handlers import http
from nameko.rpc import rpc
from nameko_sqlalchemy import DatabaseSession
from ticket.models import DeclarativeBase, Ticket
from ticket.schemas import TicketSchema
from nameko.exceptions import BadRequest


class TicketService:
    name = "ticket"
    db = DatabaseSession(DeclarativeBase)

    @http('POST', '/ticket')
    def create_ticket(self, request):
        schema = TicketSchema(strict=True)
        try:
            ticket_data = schema.loads(request.get_data(as_text=True)).data
        except ValueError as exc:
            raise BadRequest("Invalid json: {}".format(exc))

        title = ticket_data['title']
        content = ticket_data['content']
        ticket = Ticket(title=title, content=content)

        self.db.add(ticket)
        self.db.commit()

        return 200

    @rpc
    def get_all_tickets(self):
        ticket = self.db.query(Ticket).order_by(Ticket.id)
        tickets = []
        for instance in ticket:
            data = dict()
            data['id'] = instance.id
            data['title'] = instance.title
            data['description'] = instance.description
            tickets.append(data)
        return json.dumps(tickets)

    @rpc
    def get_ticket(self, ticket_id):
        ticket = self.db.query(Ticket).filter(Ticket.id == ticket_id).first()
        if not ticket:
            raise ValueError(f'Ticket with id {ticket_id} not found')
        return TicketSchema().dump(ticket).data
