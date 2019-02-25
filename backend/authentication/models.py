"""
Persistence for domain entities
"""

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import validate_email
from django.db import models
from django.utils import timezone
from rolepermissions.roles import get_user_roles #Paquete

from backend.authentication import managers
from backend.authentication.apps import AuthenticationConfig
from backend.authentication.domain.entities import User
from backend.authentication.domain.value_objects import UserData, AccountData, Role
from backend.authentication.validators import username_validator
from backend.shared.infrastructure.mappers import EntityMapper


class UserORM(PermissionsMixin, AbstractBaseUser, EntityMapper):
    """
    Custom user for django application.
    It will store local and LDAP users, but will only store passwords for local.
    """
    username = models.CharField(max_length=25, unique=True, null=False, blank=False,
                                help_text=('Required. 25 characters or fewer.'
                                           ' Letters, digits and ./_/ -.'),
                                validators=[username_validator],
                                error_messages={
                                    'unique': 'An user with that username already exists.'
                                })

    password = models.CharField(verbose_name='Password', max_length=128, null=True)

    email = models.EmailField(verbose_name='E-mail address', max_length=70, unique=True,
                              validators=[validate_email],
                              help_text=('Required. 70 characters or fewer.'
                                         ' Email valid characters only.'),
                              error_messages={
                                  'unique': 'This email has an account already assigned.'
                              })

    name = models.CharField(verbose_name='Name', max_length=40, null=False, blank=True,
                            help_text='40 characters or fewer. Name of the user')

    last_name = models.CharField(verbose_name='Last name', max_length=50, blank=True,
                                 help_text='50 characters or fewer. Surname of the user')

    is_local = models.BooleanField(verbose_name='Local account', default=True,
                                   help_text=('Designates whether the user is local or '
                                              'should be logged against external resource'))

    is_admin = models.BooleanField(verbose_name='Admin account', default=False,
                                   help_text=('Designates whether the user can '
                                              'log into this admin site.'))

    is_active = models.BooleanField(verbose_name='Active status', default=True,
                                    help_text=('Designates whether this user should be '
                                               'treated as active. Deselect this instead'
                                               ' of deleting accounts.'))

    date_joined = models.DateTimeField(verbose_name='Date when user account was created',
                                       default=timezone.now)

    objects = managers.UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password', 'email']

    class Meta:
        db_table = '{0}_user'.format(AuthenticationConfig.name)
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        full_name = ' '.join([self.name, self.last_name]).strip()
        return full_name if self.name else self.get_short_name()

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.username

    # TODO: edit this function to let user enter or not to module
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    # TODO: edit this function to let user execute or not some action
    def has_perm(self, perm, obj=None):
        return True

    @property
    def is_staff(self):
        """ Function used by Django to determine whether an user can enter
         the admin site or not"""
        return self.is_admin

    #Esto parece importante
    @property
    def entity(self) -> User:
        user_data = UserData(email=self.email,
                             username=self.username, password=self.password,
                             name=self.name, last_name=self.last_name)

        account_data = AccountData(is_active=self.is_active, is_local=self.is_local,
                                   is_admin=self.is_admin, date_joined=self.date_joined,
                                   last_login=self.last_login)

        roles = [
            Role(
                name=role.get_name(),
                permissions=[
                    permission
                    for permission
                    in role.permissions
                ])
            for role in get_user_roles(self)
        ]

        return User(id=self.id, user_data=user_data, account_data=account_data, roles=roles)

    @classmethod
    def create_from_entity(cls, entity):
        return cls(id=entity.id, email=entity.user_data.email,
                   username=entity.user_data.username,
                   password=entity.user_data.password,
                   name=entity.user_data.name,
                   last_name=entity.user_data.last_name,
                   is_active=entity.account_data.is_active,
                   is_local=entity.account_data.is_local,
                   is_admin=entity.account_data.is_admin,
                   date_joined=entity.account_data.date_joined or timezone.datetime.now(),
                   last_login=entity.account_data.last_login)
