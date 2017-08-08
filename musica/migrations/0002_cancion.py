# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-29 23:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musica', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cancion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveSmallIntegerField()),
                ('nombre', models.CharField(max_length=30)),
                ('comp_musica', models.CharField(max_length=30)),
                ('comp_letra', models.CharField(default='Kevin Calvo', max_length=15)),
                ('letra', models.TextField()),
            ],
        ),
    ]
