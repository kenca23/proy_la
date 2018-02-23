#!/usr/bin/python3
# This Python file uses the following encoding: utf-8
from django.db import models

# Create your models here.


class Disco(models.Model):
    nombre = models.CharField(max_length=30,)
    nombDisco = models.CharField(max_length=30,)
    fecha_salida = models.DateField(auto_now=False, auto_now_add=False,)
    anno = models.PositiveSmallIntegerField()
    nombre_banda = models.CharField(max_length=15,default="Lalalá")
    integrantes= models.CharField(max_length=50,default="Kevin Calvo, Kenneth Calvo, Roberto Cruz")
    info= models.TextField()
    imagen = models.ImageField(upload_to='media/Discos/')
    imagen_grande = models.ImageField(upload_to='media/Discos/')
    playlist_spotify = models.CharField(max_length=45, )

    def __str__(self):
        return str(self.nombre)

    def __unicode__(self):
        return str(self.nombre)



class Cancion(models.Model):
	disco = models.ForeignKey(Disco, on_delete=models.CASCADE)
	numero = models.PositiveSmallIntegerField()
	nombre = models.CharField(max_length=30, )
	comp_musica = models.CharField(max_length=30, )
	comp_letra = models.CharField(max_length=15,default="Kevin Calvo")
	letra= models.TextField()

	def __str__(self):
		return str(self.nombre)

	def __unicode__(self):
		return str(self.nombre)
	

class Ficha_Tecnica(models.Model):
    disco = models.ForeignKey(Disco, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30, )
    valor= models.TextField()
    
    def __str__(self):
        return str(self.nombre + ' : ' + self.valor)

    def __unicode__(self):
        return str(self.nombre + ' : ' + self.valor)
		

#class Sencillo(models.Model):
#    nombre = models.CharField(max_length=45, )
#    imagen = models.ImageField(upload_to='media/imagen_sencillo/')
#    fecha_salida = models.DateField(auto_now=False, auto_now_add=False,)
#    info= models.TextField()
#    nombre_banda = models.CharField(max_length=15,default="Lalalá")
#    letra= models.TextField()
#    comp_musica = models.CharField(max_length=30, )
#    comp_letra = models.CharField(max_length=15,default="Kevin Calvo")
#    track_spotify = models.CharField(max_length=45, )
    
#    def __str__(self):
#        return str(self.nombre)
    
#    def __unicode__(self):
#        return str(self.nombre)
        
#class Ficha_Tecnica_Sencillo(models.Model):
#    sencillo = models.ForeignKey(Sencillo, on_delete=models.CASCADE)
#    nombre = models.CharField(max_length=30, )
#    valor= models.TextField()
#    
#    def __str__(self):
#        return str(self.nombre + ' : ' + self.valor)

#    def __unicode__(self):
#        return str(self.nombre + ' : ' + self.valor)
    
class Disponible_En_Disco(models.Model):
    SPOTIFY = 'Spotify'
    DEEZER = 'Deezer'
    APMUSIC = 'Apple Music'
    AMMUSIC = 'Amazon Music'
    YOUTUBE = 'YouTube'
    
    DISPONIBLE = (
        (SPOTIFY, 'Spotify'),
        (DEEZER, 'Deezer'),
        (APMUSIC, 'Apple Music'),
        (AMMUSIC, 'Amazon Music'),
        (YOUTUBE, 'YouTube'),
    )
    
    disco = models.ForeignKey(Disco, on_delete=models.CASCADE)
    plataforma = models.CharField(
        max_length=15,
        choices=DISPONIBLE,
        default=SPOTIFY,
    )
    link = models.URLField(max_length=200,)
    
    def __str__(self):
        return str(str(self.disco) + ' : ' + self.plataforma)

    def __unicode__(self):
        return str(str(self.disco) + ' : ' + self.plataforma)
        
class Video(models.Model):
    nombre = models.CharField(max_length=75, )
    url = models.CharField(max_length=50, )
    fecha_salida = models.DateField(auto_now=False, auto_now_add=False,)
    

    def __str__(self):
        return str(self.nombre)

    def __unicode__(self):
        return str(self.nombre)
        
class SmartLink(models.Model):
    nombre = models.CharField(max_length=75,)
    nombSmart = models.CharField(max_length=75,)
    imagen = models.ImageField(upload_to='media/smartLink/')
    colorFondo = models.CharField(max_length=6,)
    
    def __str__(self):
        return str(self.nombre)

    def __unicode__(self):
        return str(self.nombre)
        
class Link_SmartLink(models.Model):
    SPOTIFY = 'Spotify'
    APMUSIC = 'Apple Music'
    ITUNES = 'iTunes'
    DEEZER = 'Deezer'
    GOOGLE = 'Google Play Music'
    BANDCAMP = 'BandCamp'
    AMMUSIC = 'Amazon Music'
    NAPSTER = 'Napster'
    
    DISPONIBLE = (
        (SPOTIFY, 'Spotify'),
        (APMUSIC, 'Apple Music'),
        (ITUNES, 'iTunes'),
        (DEEZER, 'Deezer'),
        (GOOGLE, 'Google Play Music'),
        (BANDCAMP, 'BandCamp'),
        (AMMUSIC, 'Amazon Music'),
        (NAPSTER, 'Napster'),
    )
    
    smartlink = models.ForeignKey(SmartLink, on_delete=models.CASCADE)
    plataforma = models.CharField(
        max_length=17,
        choices=DISPONIBLE,
        default=SPOTIFY,
    )
    link = models.CharField(max_length=200,)
    
    def __str__(self):
        return str(str(self.smartlink) + ' : ' + self.plataforma)

    def __unicode__(self):
        return str(str(self.smartlink) + ' : ' + self.plataforma)