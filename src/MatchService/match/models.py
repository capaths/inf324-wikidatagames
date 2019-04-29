"""Match Models"""


class Match:
    """Match Model"""
    n_turns: int
    end: bool

    def __init__(self, n_turns: int, end:bool):
        self.n_turns = n_turns
        self.end = end
