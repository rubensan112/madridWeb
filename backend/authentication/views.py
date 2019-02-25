import settings
from backend.authentication import forms, services
from backend.authentication.application import interactors
from backend.shared.infrastructure.views import View

#TODO forms, e interactors compeltado. Queda el service.
class LoginView(View):
    form = forms.LoginForm
    service = services.AuthenticationService
    interactor = interactors.LoginUserInteractor
    template_name = 'login.html'

    def get(self, request, **kwargs):
        if request.user.is_authenticated:
            return self.redirect_to_url(settings.LOGIN_REDIRECT_URL)

        interactor_result = self.interactor(form=self.form(),
                                            service=self.service(request)).execute()

        return self.render_template(request, template_name=self.template_name,
                                    context=interactor_result.context or {})

    def post(self, request, **kwargs):
        form_filled = self.form(request.POST.dict())
        interactor_result = self.interactor(form=form_filled or None,
                                            service=self.service(request)).execute()

        if interactor_result.success:
            return self.redirect_to_url(settings.LOGIN_REDIRECT_URL)

        return self.render_template(request, template_name=self.template_name,
                                    context=interactor_result.context or {})


class LogoutView(View):
    interactor = interactors.LogoutUserInteractor
    service = services.AuthenticationService

    def get(self, request, **kwargs):
        self.interactor(service=self.service(request)).execute()
        return self.redirect_to_url(settings.LOGIN_URL)
