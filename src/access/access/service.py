"""Access Service"""

from nameko.rpc import rpc
import jwt

from .secret import JWT_SECRET


class NotAuthenticated(Exception):
    pass


class AccessService:
    name = 'access'

    @rpc
    def login(self, username, password):
        if password == "secret":
            token = jwt.encode({
                'username': username,
                'permissions': [],
                'roles': []
            }, JWT_SECRET)
            return token
        raise NotAuthenticated()

    @rpc
    def signup(self, username, password):
        # TODO: Implement
        return self.login(username, password)
