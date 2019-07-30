"""Chat Service"""

from nameko.web.websocket import WebSocketHubProvider, rpc
from nameko.web.handlers import http
from nameko.extensions import DependencyProvider


class Config(DependencyProvider):
    def get_dependency(self, worker_ctx):
        return self.container.config


class ContainerIdentifier(DependencyProvider):
    "To identify worker"

    def get_dependency(self, worker_ctx):
        return id(self.container)


class ChatService:
    name = "chat"

    container_id = ContainerIdentifier()
    websocket_hub = WebSocketHubProvider()
    config = Config()

    @rpc
    def subscribe(self, socket_id):
        self.websocket_hub.subscribe(socket_id, 'test_channel')
        return 'subscribed to test_channel'
