"""
Backends to allow Django use their internal auth and session system.
Every backend should only implement a mehtod called authenticate and other called
get_user.
"""

from django.contrib.auth.backends import ModelBackend

from backend.authentication.domain.entities import User
from backend.authentication.models import UserORM
from backend.authentication.repositories import UserDatabaseRepository


class LocalUsersBackend(ModelBackend):
    """
    Authenticates local users in the application
    """
    def authenticate(self, request=None, username=None, password=None, **kwargs):
        user = super().authenticate(request, username, password, **kwargs)
        if user and user.entity.account_data.is_local and user.entity.user_data.password:
            return user

        return None

