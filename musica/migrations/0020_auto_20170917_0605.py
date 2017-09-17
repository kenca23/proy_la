# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-17 06:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('musica', '0019_auto_20170917_0601'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='fecha_salida',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='video',
            name='nombre',
            field=models.CharField(max_length=75),
        ),
    ]