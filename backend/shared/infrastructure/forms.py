from django import forms


class Form(forms.Form):
    @property
    def valid_data(self) -> dict:
        return self.cleaned_data

    @property
    def is_valid(self) -> bool:
        return super().is_valid()
