from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.db import models


# Create your models here.


class District(models.Model):
    district = models.PositiveIntegerField(unique=True,
                                           blank=True,
                                           null=True,
                                           verbose_name="Участок",
                                           default=1)
    class Meta:
        verbose_name = "Участок"
        verbose_name_plural = "Участки"

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50,
                                unique=True,
                                blank=False,
                                null=False,
                                verbose_name="Имя пользователя")
    password = models.CharField(max_length=128, verbose_name="Пароль")
    first_name = models.CharField(max_length=50,
                                  blank=True,
                                  null=False,
                                  verbose_name="Имя")
    last_name = models.CharField(max_length=50,
                                 blank=True,
                                 null=False,
                                 verbose_name="Фамилия")
    is_staff = models.BooleanField(default=False,
                                   verbose_name="Сотрудник")
    is_active = models.BooleanField(default=True,
                                    verbose_name="Активность")
    is_superuser = models.BooleanField(default=False)
    email = models.EmailField(max_length=50,
                              unique=True,
                              blank=False,
                              null=False,
                              verbose_name="Почта")
    district = models.ForeignKey(District, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name="Участок")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email", "password", ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}, участок №{self.district}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
