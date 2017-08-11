# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-11 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0002_auto_20170811_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen_pagina',
            name='nombre',
            field=models.CharField(choices=[('DIS', 'Discografía'), ('CAL', 'Calendario'), ('PRE', 'Prensa'), ('CON', 'Contacto'), ('GRA', 'Gracias')], default='DIS', max_length=3),
        ),
    ]
