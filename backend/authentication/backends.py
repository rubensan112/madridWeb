"""
Backends to allow Django use their internal auth and session system.
Every backend should only implement a mehtod called authenticate and other called
get_user.
"""

from django.contrib.auth.backends import ModelBackend

from backend.authentication.domain.entities import User
from backend.authentication.models import UserORM
from backend.authentication.repositories import UserDatabaseRepository
from backend.authentication.services import LDAPService, UserService


class LocalUsersBackend(ModelBackend):
    """
    Authenticates local users in the application
    """
    def authenticate(self, request=None, username=None, password=None, **kwargs):
        user = super().authenticate(request, username, password, **kwargs)
        if user and user.entity.account_data.is_local and user.entity.user_data.password:
            return user

        return None


class LDAPBackend:
    """
    Authenticates users against LDAP server
    """
    def __init__(self):
        self.user_repository = UserDatabaseRepository()
        self.user_service = UserService()

    def authenticate(self, request=None, username=None, password=None):
        ldap_service = LDAPService()
        ldap_service.connect()
        user_data = ldap_service.fetch_user_data_by_username(username)

        if not user_data:
            return None

        user_dn = ldap_service.compose_dn_from_uid((user_data['uid']))
        auth_successful = ldap_service.user_authenticate(user_dn, password)

        if not auth_successful:
            return None

        user: User = self.user_service.get_or_create_external_user(
            username=username,
            email=str(user_data['mail']),
            name=self._get_name_from_user_data(user_data),
            last_name=str(user_data['sn'])
        )

        if not user.account_data.is_active:
            return None

        return UserORM.create_from_entity(user) # Creo que con esto crea un usuario nuevo dentro del otro backend.

    def get_user(self, user_id):
        user = self.user_repository.find_one_by_id(user_id)  # type: User
        return UserORM.create_from_entity(user) if user.account_data.is_active else None

    def _get_name_from_user_data(self, user_data):
        complete_name = str(user_data['cn'])
        surname = str(user_data['sn'])
        name = complete_name[0:complete_name.index(surname)].rstrip()
        return name
        
