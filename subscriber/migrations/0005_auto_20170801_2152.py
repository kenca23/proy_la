# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriber', '0004_auto_20170801_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='ciudad',
            field=models.CharField(blank=True, max_length=30, verbose_name='Ciudad'),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='pais',
            field=models.CharField(blank=True, max_length=30, verbose_name='País'),
        ),
    ]
