# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-29 23:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musica', '0003_cancion_disco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disco',
            name='integrantes',
            field=models.CharField(default='Kevin Calvo, Kenneth Calvo, Roberto Cruz', max_length=50),
        ),
    ]
