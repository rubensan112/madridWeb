"""
Application services (use cases) for authentication application
"""
from backend.shared.application.interactors import InteractorResponse


class LoginUserInteractor:
    """
    Logs an user in both in internal and external applications
    """
    def __init__(self, form, service):
        self.form = form
        self.service = service

    # TODO: remove django implementations from domain!
    def execute(self):
        """
        Executes use case
        :return: InteractorResponse
        """
        login_has_succeeded = False
        if self.form.is_valid:
            username = self.form.valid_data.get("username")
            password = self.form.valid_data.get("password")

            login_has_succeeded = self.service.try_login(username, password)

            #if login_has_succeeded:
                #self.service.login_external_resources(username)

            if not login_has_succeeded:
                self.form.add_login_errors()

        context = {"form": self.form}

        return InteractorResponse(context=context, success=login_has_succeeded)


class LogoutUserInteractor:
    """
    Logs an user out in both in internal and external applications
    """
    def __init__(self, service):
        self.service = service

    def execute(self):
        """
        Executes use case
        :return: InteractorResponse
        """
        #self.service.logout_external_resources()
        self.service.try_logout()

        return InteractorResponse(success=True)
