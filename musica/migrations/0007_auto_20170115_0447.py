# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-15 10:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musica', '0006_auto_20170115_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disco',
            name='imagen',
            field=models.ImageField(upload_to='media/Discos/'),
        ),
    ]
