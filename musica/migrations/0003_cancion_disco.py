# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-29 23:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musica', '0002_cancion'),
    ]

    operations = [
        migrations.AddField(
            model_name='cancion',
            name='disco',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='musica.Disco'),
            preserve_default=False,
        ),
    ]