"""
Implementation of domain services
"""
import os

import requests
from django.contrib.auth import authenticate, login, logout

import settings
from backend.authentication.domain.entities import User
from backend.authentication.domain.value_objects import UserData, AccountData
from backend.authentication.repositories import UserDatabaseRepository
#from backend.nso.domain.exceptions import NsoError
#from backend.nso.session import Nso, get_nso_credentials_for_user



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