from authapp.views import LoginPageView
from django.urls import path
app_name = "authapp"

urlpatterns = [
    path("login/", LoginPageView.as_view(), name="login"),
]