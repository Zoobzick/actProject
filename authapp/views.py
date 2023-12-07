from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import resolve

from .forms import UserLoginForm


# Create your views here.


class LoginPageView(LoginView):
    template_name = "authapp/login.html"
    form_class = UserLoginForm

    redirect_field_name = "asdsad"
    next_page = "authapp:fake"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Авторизация"
        return context


    def get_default_redirect_url(self):
        return resolve('act:""')



