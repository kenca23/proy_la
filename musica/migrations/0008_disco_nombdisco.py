# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-12 05:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('musica', '0007_auto_20170115_0447'),
    ]

    operations = [
        migrations.AddField(
            model_name='disco',
            name='nombDisco',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]
