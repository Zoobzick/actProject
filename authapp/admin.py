from django.contrib import admin

from .models import CustomUser, District


# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    # list_display = ["Имя", "Фамилия", "Участок", "username", "email", ]
    pass


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    pass
