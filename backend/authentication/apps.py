""" Contains basic Django configurations for the application"""

from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    name = 'backend.authentication'
    verbose_name = "Authentication"
