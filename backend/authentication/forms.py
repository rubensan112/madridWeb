from django import forms

from backend.shared.infrastructure.forms import Form


class LoginForm(Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(min_length=3, widget=forms.PasswordInput)

    def add_login_errors(self):
        self.add_error("username", "Username of password incorrect")
        self.add_error("password", "Username of password incorrect")
