"""Access Service"""


class AccessService:
    """Access Service"""

    def __init__(self, app, user_repository):
        self.user_repository = user_repository

    def login_user(self, user):
        """Logs in user"""

    def logout_current_user(self):
        """Logs out user"""

    def get_current_user(self):
        """Get current user"""
