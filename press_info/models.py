from django.db import models

# Create your models here.

class Press_Info(models.Model):
    biografia= models.TextField()
    propuesta_musical= models.TextField()
    fecha_salida=models.DateField(auto_now=True, auto_now_add=False,)

    def __str__(self):
        return str(self.fecha_salida)

    def __unicode__(self):
        return str(self.fecha_salida)
    
    class Meta:
        ordering = ["-fecha_salida"]
        
class Integrante(models.Model):
    nombre = models.CharField('Nombre',max_length=30,)
    instrumento = models.CharField('Instrumento',max_length=30,)
    imagen = models.ImageField(upload_to='media/integrante/')
    fecha_salida = models.DateField(auto_now=False, auto_now_add=False,)
    id_pagina = models.CharField('Id_pagina',max_length=30,)
    biografia = models.TextField()
    
    def __str__(self):
        return str(self.nombre + ' : ' + str(self.fecha_salida))
        
    def __unicode__(self):
        return str(self.nombre + ' : ' + str(self.fecha_salida))
        
    class Meta:
        ordering = ["-fecha_salida"]
        
class Foto(models.Model):
    nombre = models.CharField('Nombre',max_length=100,)
    descripcion = models.CharField('Descripción',max_length=200,null=True,blank=True,)
    imagen = models.ImageField(upload_to='media/imagen_prensa/')
    fecha_salida = models.DateField(auto_now=False, auto_now_add=False,)
    updated = models.DateField(auto_now=True, auto_now_add=False,)
    
    def __str__(self):
        return str(self.nombre + ' : ' + str(self.fecha_salida))
        
    def __unicode__(self):
        return str(self.nombre + ' : ' + str(self.fecha_salida))
        
    class Meta:
        ordering = ["-fecha_salida"]
        
        
class Video(models.Model):
    nombre = models.CharField(max_length=75, )
    url = models.CharField(max_length=50, )
    fecha_salida = models.DateField(auto_now=False, auto_now_add=False,)
    

    def __str__(self):
        return str(self.nombre)

    def __unicode__(self):
        return str(self.nombre)
        
    class Meta:
        ordering = ["-fecha_salida"]
        
class Enlace(models.Model):
    nombre = models.CharField(max_length=75, )
    url = models.CharField(max_length=200, )
    fecha_salida = models.DateField(auto_now=False, auto_now_add=False,)
    

    def __str__(self):
        return str(self.nombre)

    def __unicode__(self):
        return str(self.nombre)
        
    class Meta:
        ordering = ["-fecha_salida"]