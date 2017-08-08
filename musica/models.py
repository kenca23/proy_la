#!/usr/bin/python3
# This Python file uses the following encoding: utf-8
from django.db import models

# Create your models here.


class Disco(models.Model):
    nombre = models.CharField(max_length=30,)
    nombDisco = models.CharField(max_length=30,)
    anno = models.PositiveSmallIntegerField()
    nombre_banda = models.CharField(max_length=15,default="Lalalá")
    integrantes= models.CharField(max_length=50,default="Kevin Calvo, Kenneth Calvo, Roberto Cruz")
    info= models.TextField()
    ficha_tecnica= models.TextField()
    imagen = models.ImageField(upload_to='media/Discos/')

    def __str__(self):
        return str(self.nombre)

    def __unicode__(self):
        return str(self.nombre)


class Cancion(models.Model):
	disco = models.ForeignKey(Disco)
	numero = models.PositiveSmallIntegerField()
	nombre = models.CharField(max_length=30, )
	comp_musica = models.CharField(max_length=30, )
	comp_letra = models.CharField(max_length=15,default="Kevin Calvo")
	letra= models.TextField()

	def __str__(self):
		return str(self.nombre)

	def __unicode__(self):
		return str(self.nombre)