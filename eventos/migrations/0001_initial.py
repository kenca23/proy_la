# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-25 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
                ('lugar', models.CharField(max_length=75)),
                ('hora', models.TimeField()),
                ('facebook', models.URLField()),
                ('twitter', models.URLField()),
                ('texto', models.TextField()),
            ],
        ),
    ]
