from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserRegistrationForm(forms.Form):
    pass


class UserLoginForm(AuthenticationForm):
    """
    Форма аутентификации пользователя
    """

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы
        """
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
        })

    def clean(self):
        print(self.request)
        print(self.cleaned_data.get("username"))
        print(self.cleaned_data.get("password"))
        return super().clean()
