# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 21:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriber', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='ciudad',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='pais',
            field=models.CharField(max_length=30, null=True),
        ),
    ]