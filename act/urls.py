from act.views import ActCreateView, ActListView
from authapp.views import LoginPageView
from django.urls import path
app_name = "act"

urlpatterns = [
    path("create/", ActCreateView.as_view(), name="create"),
    path("list/", ActListView.as_view(), name="list")
]