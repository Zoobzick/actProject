from django.db import models


# Create your models here.
class Area(models.Model):
    """ Модель Объекта"""
    area_name = models.CharField(null=False,
                                 blank=False,
                                 unique=True,
                                 max_length=512,
                                 verbose_name="Наименование объекта")
    area_short_name = models.CharField(null=False,
                                       blank=False,
                                       unique=True,
                                       max_length=256,
                                       verbose_name="Сокращенное наименование объекта")

    class Meta:
        verbose_name = "Объект"
        verbose_name_plural = "Объекты"


class Project(models.Model):
    """ Модель Шифра проекта"""
    project_name = models.CharField(null=False,
                                    blank=False,
                                    unique=True,
                                    max_length=256,
                                    verbose_name="Шифр проекта")
    area = models.ForeignKey(Area, on_delete=models.DO_NOTHING, verbose_name="Объект")

    class Meta:
        verbose_name = "Шифр проекта"
        verbose_name_plural = "Шифры проектов"


class Scheme(models.Model):
    """ Модель исполнительной схемы"""
    name = models.CharField(null=False,
                            blank=False,
                            max_length=256,
                            verbose_name="Наименование")
    date = models.DateField(null=False,
                            blank=False,
                            verbose_name="Дата")
    job_name = models.CharField(max_length=256,
                                verbose_name="Выполненные работы")
    amount_of_work = models.PositiveIntegerField(null=False,
                                                 blank=False,
                                                 )
    project = models.ManyToManyField(Project,
                                     blank=False,
                                    )

    class Meta:
        verbose_name = "Исполнительная схема"
        verbose_name_plural = "Исполнительные схемы"


class Act(models.Model):
    """ Модель АОСР """
    name = models.CharField(max_length=25,
                            null=False,
                            blank=False,
                            verbose_name="№ акта")

    schema = models.ForeignKey(Scheme,
                               blank=False,
                               null=False,
                               on_delete=models.DO_NOTHING)
    date = models.DateField(blank=False,
                            null=False,
                            verbose_name="Дата акта")
    is_signed = models.BooleanField(default=False,
                                    verbose_name="Подписан")

    class Meta:
        verbose_name = "АОСР"
        verbose_name_plural = "АОСР"

    def __str__(self):
        return f"АОСР №{self.name} от {self.date}"


class Material(models.Model):
    """ Модель Материалов"""
    name = models.CharField(null=False,
                            blank=False,
                            max_length=256,
                            verbose_name="Наименование")

    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"
