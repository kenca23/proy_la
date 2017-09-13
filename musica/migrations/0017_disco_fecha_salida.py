# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-10 20:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('musica', '0016_sencillo_nombre_banda'),
    ]

    operations = [
        migrations.AddField(
            model_name='disco',
            name='fecha_salida',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
