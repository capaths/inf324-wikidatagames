"""Ticket Service"""
from __future__ import absolute_import

import json
from nameko.rpc import rpc
from nameko.web.handlers import http
from ticket.models import TicketDatabase, Ticket
from ticket.schemas import TicketSchema


class TicketService:
    name = "ticket"
    rep = TicketDatabase()

    def create_ticket(self, title, content):
        ticket = Ticket(title=title, content=content)

        try:
            self.rep.db.add(ticket)
            self.rep.db.commit()
        except:
            self.rep.db.rollback()
            return False

        return True

    def get_ticket(self, ticket_id):
        ticket = Ticket(id=ticket_id)

        self.rep.db.add(ticket)
        self.rep.db.commit()

    def get_all_tickets(self):
        ticket = self.rep.db.query(Ticket).order_by(Ticket.id)
        tickets = []
        for instance in ticket:
            data = dict()
            data['id'] = instance.id
            data['title'] = instance.title
            data['content'] = instance.content
            tickets.append(data)
        return tickets

    @http('POST', '/ticket')
    def post_ticket(self, request):
        schema = TicketSchema(strict=True)
        try:
            ticket_data = schema.loads(request.get_data(as_text=True)).data
        except ValueError:
            return 400

        title = ticket_data['title']
        content = ticket_data['content']

        self.create_ticket(title, content)
        return 200

    @http('GET', '/ticket')
    def get_tickets(self, request):
        return json.dumps(self.get_all_tickets())
