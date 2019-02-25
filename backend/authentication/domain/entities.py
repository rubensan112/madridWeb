"""
Domain entities for authentication application
"""
from typing import List

from backend.authentication.domain import exceptions, value_objects
from backend.shared.domain.entities import DomainEntity


class User(DomainEntity):
    """
    Represents the domain data related to an user that can log in the application
    """
    def __init__(self, user_data: value_objects.UserData,
                 account_data: value_objects.AccountData,
                 id: int = None, roles: List[value_objects.Role] = None):

        if account_data.is_local and not user_data.password:
            raise exceptions.LocalUserPasswordUnsetError

        self.id = id
        self.user_data = user_data
        self.account_data = account_data
        self.roles = roles if roles is not None else []

    def has_role(self, role: str) -> bool:
        """
        Checks if a user has a concrete role
        :param role: str
        :return: bool
        """
        return role in [role.name for role in self.roles]

    def has_permission(self, permission: str) -> bool:
        """
        Checks if a user has a concrete permission
        :param permission: str
        :return: bool
        """
        return permission in self.permissions

    @property
    def permissions(self) -> List:
        """
        Property that returns all permissions of user
        :return: List
        """
        permissions = []
        for perms in [role.permissions for role in self.roles]:
            permissions.extend(x for x in perms if x not in permissions)

        return permissions

    def get_full_name(self):
        """
        Returns complete name of user (if possible)
        :return: str
        """
        full_name = ' '.join([self.user_data.name, self.user_data.last_name]).strip()
        return full_name if self.user_data.name else self.get_short_name()

    def get_short_name(self):
        """
        Return short_name of user (username)
        :return:
        """
        return self.user_data.username

    @classmethod
    def create_from_dict(cls, entity_data: dict):
        """
        Creates an user class from data in dictionary
        :param entity_data: dict
        :return: User
        """
        user_data = value_objects.UserData.create_from_dict(
            entity_data.get('user_data', entity_data)
        )

        account_data = value_objects.AccountData.create_from_dict(
            entity_data.get('account_data', entity_data)
        )

        return cls(id=entity_data.get('id', None),
                   user_data=user_data,
                   account_data=account_data)

    @property
    def as_dict(self) -> dict:
        """
        Parses user entity has dict
        :return: dict
        """
        return dict(id=self.id, user_data=self.user_data.as_dict,
                    account_data=self.account_data.as_dict,
                    roles=[role.as_dict for role in self.roles])
