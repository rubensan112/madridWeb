"""
Implementation of domain services
"""
import os

import requests
from django.contrib.auth import authenticate, login, logout
from ldap3 import Server, Connection, ALL, Tls

import settings
from backend.authentication.domain.entities import User
from backend.authentication.domain.value_objects import UserData, AccountData
from backend.authentication.repositories import UserDatabaseRepository
#from backend.nso.domain.exceptions import NsoError
#from backend.nso.session import Nso, get_nso_credentials_for_user


class LDAPService:
    connection = None

    def __init__(self):
        ca_cert_path = settings.LDAP_CERT_PATH

        tls = Tls(ca_certs_path=ca_cert_path)

        self.ldap_servers = [
            Server(host=host, port=port, get_info=ALL, use_ssl=False, tls=tls)
            for host, port in settings.LDAP_INSTANCES
        ]

        self.user_ldap_attributes = ['mail', 'cn', 'sn', 'uid', 'userPassword']

    def connect(self):
        self._reset_connection()

    def _reset_connection(self):
        self.connection = Connection(server=self.ldap_servers,
                                     user=settings.LDAP_ADMIN_USERNAME,
                                     password=settings.LDAP_ADMIN_PASSWORD,
                                     auto_bind=True)

    def fetch_user_data_by_username(self, username: str, attributes: list = None):
        if attributes is None:
            attributes = self.user_ldap_attributes

        self.connection.search(search_base=settings.LDAP_SEARCH_BASE,
                               search_filter='(uid={0})'.format(username),
                               attributes=attributes)

        if not self.connection.entries:
            return None

        ldap_user_data = self.connection.entries[0]

        return ldap_user_data

    def user_authenticate(self, user_dn, password):
        self.connection.user = user_dn
        self.connection.password = password
        user_bind = self.connection.bind()
        self._reset_connection()

        return user_bind

    @staticmethod
    def compose_dn_from_uid(uid):
        return "uid={uid},{base_dn}".format(uid=uid, base_dn=settings.LDAP_SEARCH_BASE)


class UserService:
    def __init__(self):
        self.user_repository = UserDatabaseRepository()

    def get_or_create_external_user(self, username, email, **other_fields):
        try:
            users_list = self.user_repository.find_by(username=username)
            user = users_list[0]
        except IndexError:
            user = None

        if not user:
            user = self.create_external_user(
                username=username,
                email=email,
                **other_fields
            )

        return user

    def create_external_user(self, username, email, name='', last_name=''):
        user_data = UserData(email=email, username=username,
                             name=name, last_name=last_name)
        account_data = AccountData(is_active=True, is_local=False)
        user = User(user_data=user_data, account_data=account_data)

        self.user_repository.save(user)

        return user


class AuthenticationService:
    def __init__(self, request):
        self.request = request

    def try_login(self, username, password):
        user = authenticate(username=username, password=password) #Aqui iterara entre las distintas backends, que hay dentro del settings.py

        if user is None:
            return False

        login(request=self.request, user=user)
        return True

    def try_logout(self):
        logout(self.request)
        return True

    '''
    def login_external_resources(self, username):
        user = UserDatabaseRepository().find_by(username=username)[0]  # type: User

        nso_user, nso_password = get_nso_credentials_for_user(user)

        try:
            return Nso.create_new_nso_session(self.request, nso_user, nso_password)
        except (requests.exceptions.ConnectionError, NsoError):
            return False

    def logout_external_resources(self):
        try:
            with Nso.create_from_request(self.request) as nso:
                nso.delete_nso_session(self.request)
        except (requests.exceptions.ConnectionError, NsoError):
            pass
    '''