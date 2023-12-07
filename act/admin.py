from django.contrib import admin

# Register your models here.
from .models import Act, Material, Scheme, Area, Project


@admin.register(Act)
class ActAdmin(admin.ModelAdmin):
    pass


@admin.register(Material)
class Materials(admin.ModelAdmin):
    pass


@admin.register(Scheme)
class Scheme(admin.ModelAdmin):
    pass


@admin.register(Area)
class Area(admin.ModelAdmin):
    list_display = ["area_name"]
    pass


@admin.register(Project)
class Project(admin.ModelAdmin):
    pass
