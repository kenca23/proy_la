# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-29 22:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bio_info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='integrante',
            name='imagen',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='media/biografia/'),
            preserve_default=False,
        ),
    ]
