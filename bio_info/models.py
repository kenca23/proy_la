from django.db import models

# Create your models here.


class Miembro(models.Model):
    nombre = models.CharField('Nombre',max_length=30,)
    instrumento = models.CharField('Instrumento',max_length=30,)
    imagen = models.ImageField(upload_to='media/biografia/')
    imagen_home = models.ImageField(upload_to='media/home/')
    imagen_prensa = models.ImageField(upload_to='media/prensa/')
    biografia = models.TextField()
    id_pagina = models.CharField('Id_pagina',max_length=30,)
    fecha_salida = models.DateField(auto_now=False, auto_now_add=False,)
    
    def __str__(self):
        return str(self.nombre + ' : ' + str(self.fecha_salida))
        
    def __unicode__(self):
        return str(self.nombre + ' : ' + str(self.fecha_salida))
        
class Banda(models.Model):
    imagen = models.ImageField(upload_to='media/biografia/')
    biografia = models.TextField()
    fecha_salida = models.DateField(auto_now=False, auto_now_add=False,)
    
    def __str__(self):
        return str(self.fecha_salida)
        
    def __unicode__(self):
        return str(self.fecha_salida)