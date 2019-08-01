"""Match Service"""

from nameko.rpc import rpc
from nameko.extensions import DependencyProvider
from nameko.web.websocket import WebSocketHubProvider, rpc

class ContainerIdentifier(DependencyProvider):
    def get_dependency(self, worker_ctx):
        return id(self.container)


class MatchService:
    name = "match"

    @rpc
    def challenge(self, user_a, user_b):
        pass

    @rpc
    def next_turn(self):
        pass
