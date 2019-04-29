"""Player Models"""


class Player:
    """Player Model"""
    name: str
    country: str
    elo: int

    def __init__(self, name: str, country: str, elo: int):
        self.name = name
        self.country = country
        elo = elo
