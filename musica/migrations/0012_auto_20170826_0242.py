# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-26 02:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musica', '0011_disco_imagen_grande'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disponible_En_Sencillo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(choices=[('SPO', 'Spotify'), ('DEE', 'Deezer'), ('APM', 'Apple Music')], default='SPO', max_length=3)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Ficha_Tecnica_Sencillo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('valor', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sencillo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('imagen', models.ImageField(upload_to='media/imagen_sencillo/')),
                ('fecha_salida', models.DateField()),
                ('info', models.TextField()),
                ('letra', models.TextField()),
                ('comp_musica', models.CharField(max_length=30)),
                ('comp_letra', models.CharField(default='Kevin Calvo', max_length=15)),
                ('track_spotify', models.CharField(max_length=45)),
                ('compartir_facebook', models.URLField()),
                ('compartir_twiter', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='ficha_tecnica_sencillo',
            name='sencillo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musica.Sencillo'),
        ),
        migrations.AddField(
            model_name='disponible_en_sencillo',
            name='sencillo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musica.Sencillo'),
        ),
    ]
