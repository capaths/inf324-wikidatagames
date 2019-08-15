"""Chat Service"""

from nameko.rpc import RpcProxy, rpc


class ChatService:
    name = "chat"

    gateway_rpc = RpcProxy("gateway")

    @rpc
    def receive_message(self, sender, content, room=None):
        # TODO: Verify if sender is a player and if it is in room (None is general)
        self.gateway_rpc.broadcast_message(sender, content, room=room)

    @rpc
    def create_room(self, room_name):
        # TODO: generate id (encryption) and make it to be saved by the user.
        pass
