from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserManagersTest(TestCase):
    User = get_user_model()
    user = User.objects.create_user(username="troover", password="foo", email="murdoc-94@mail.ru")
