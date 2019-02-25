"""
Value objects. Objects corresponding domain.
"""
import datetime
from typing import List

from backend.shared.domain.value_objects import ValueObject


class UserData(ValueObject):
    """
    Value objects that represents application's user data.
    """
    def __init__(self, email: str, username: str, password: str = None,
                 name: str = None, last_name: str = None):
        self.email = email
        self.username = username
        self.password = password
        self.name = name
        self.last_name = last_name

    @classmethod
    def create_from_dict(cls, object_data: dict):
        """
        Creates the value object from dict
        :param object_data: dict
        :return: UserData
        """
        return cls(email=object_data.get('email'),
                   username=object_data.get('username'),
                   password=object_data.get('password', None),
                   name=object_data.get('name', None),
                   last_name=object_data.get('last_name', None))

    @property
    def as_dict(self) -> dict:
        """
        Parses object as dict
        :return: dict
        """
        return dict(email=self.email, name=self.name, last_name=self.last_name,
                    username=self.username, password=self.password)


class AccountData(ValueObject):
    """
    Value objects that represents application's user account data.
    """
    def __init__(self, is_active: bool, is_local: bool = False, is_admin: bool = False,
                 date_joined: datetime = None, last_login: datetime = None):
        self.is_active = is_active
        self.is_local = is_local
        self.is_admin = is_admin
        self.date_joined = date_joined
        self.last_login = last_login

    @classmethod
    def create_from_dict(cls, object_data: dict):
        """
        Creates the value object from dict
        :param object_data: dict
        :return: AccountData
        """
        return cls(is_active=object_data.get('is_active'),
                   is_local=object_data.get('is_local', False),
                   is_admin=object_data.get('is_admin', False),
                   date_joined=object_data.get('date_joined', None),
                   last_login=object_data.get('last_login', None))

    @property
    def as_dict(self) -> dict:
        """
        Parses object as dict
        :return: dict
        """
        return dict(is_active=self.is_active, is_local=self.is_local,
                    is_admin=self.is_admin, date_joined=self.date_joined,
                    last_login=self.last_login)


class Role(ValueObject):
    """
    Value objects that represents application's user role.
    """
    def __init__(self, name, permissions: List[str] = None):
        self.name = name
        self.permissions = permissions if permissions is not None else []

    @classmethod
    def create_from_dict(cls, object_data: dict):
        """
        Creates the value object from dict
        :param object_data: dict
        :return: UserData
        """
        return cls(name=object_data.get('name'),
                   permissions=object_data.get('permissions'))

    @property
    def as_dict(self) -> dict:
        """
        Parses object as dict
        :return: dict
        """
        return dict(name=self.name, permissions=self.permissions)
