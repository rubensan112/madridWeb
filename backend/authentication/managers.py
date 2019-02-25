from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username: str, email: str, password: str = None,
                    commit: bool = True, **extra_fields):
        """
        Creates and saves an User with the given username and email.
        If password is specified, password is set and sets flag
        is_local to True.

        :param username: str
        :param email: str
        :param password: str
        :param commit: bool
        :param extra_fields:
        :return: User
        """
        if not username or not email:
            raise ValueError('Username and email fields cannot be empty.')

        email_normalized = self.normalize_email(email)
        username_normalized = self.model.normalize_username(username)
        user = self.model(username=username_normalized, email=email_normalized,
                          **extra_fields)

        if password:
            user.set_password(password)

        if not password:
            user.is_local = False

        if commit:
            self.save(user)

        return user

    def create_superuser(self, username: str, email: str, password: str = None,
                         commit: bool = True, **extra_fields):
        """
        Creates and saves a superuser with the given email and username.

        :param username: str
        :param email: str
        :param password: str
        :param commit: bool
        :param extra_fields:
        :return: User
        """
        extra_fields.setdefault('is_admin', True)

        if extra_fields.get('is_admin') is not True:
            raise ValueError('Superuser must have is_admin flag set to True')

        return self.create_user(username=username, email=email, password=password,
                                commit=commit, **extra_fields)

    def save(self, user):
        """
        Persits user in database
        :param user: User
        :return: User
        """
        user.save(using=self._db)
        return user
