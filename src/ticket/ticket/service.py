"""Player Service"""
from nameko.rpc import rpc


class TicketService:
    name = "ticket"

    @rpc
    def send_ticket(self, user, name, content):
        pass
