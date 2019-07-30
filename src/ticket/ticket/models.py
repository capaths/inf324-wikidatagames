"""Ticket Models"""


class Ticket:
    """Ticket Model"""
    name: str
    description: int

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
