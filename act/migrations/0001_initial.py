# Generated by Django 4.2.4 on 2023-12-05 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(max_length=512, unique=True, verbose_name='Наименование объекта')),
                ('area_short_name', models.CharField(max_length=256, unique=True, verbose_name='Сокращенное наименование объекта')),
            ],
            options={
                'verbose_name': 'Объект',
                'verbose_name_plural': 'Объекты',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Материал',
                'verbose_name_plural': 'Материалы',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=256, unique=True, verbose_name='Шифр проекта')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='act.area', verbose_name='Объект')),
            ],
            options={
                'verbose_name': 'Шифр проекта',
                'verbose_name_plural': 'Шифры проектов',
            },
        ),
        migrations.CreateModel(
            name='Scheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Наименование')),
                ('date', models.DateField(verbose_name='Дата')),
                ('job_name', models.CharField(max_length=256, verbose_name='Выполненные работы')),
                ('amount_of_work', models.PositiveIntegerField()),
                ('project', models.ManyToManyField(to='act.project')),
            ],
            options={
                'verbose_name': 'Исполнительная схема',
                'verbose_name_plural': 'Исполнительные схемы',
            },
        ),
        migrations.CreateModel(
            name='Act',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='№ акта')),
                ('date', models.DateField(verbose_name='Дата акта')),
                ('is_signed', models.BooleanField(default=False, verbose_name='Подписан')),
                ('schema', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='act.scheme')),
            ],
            options={
                'verbose_name': 'АОСР',
                'verbose_name_plural': 'АОСР',
            },
        ),
    ]
