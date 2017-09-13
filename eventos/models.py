from django.db import models

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=75, )
    linkEvento = models.CharField(max_length=75,default="")
    fecha = models.DateField(auto_now=False, auto_now_add=False, )
    lugar = models.CharField(max_length=75, )
    hora = models.TimeField(auto_now=False, auto_now_add=False, )
    facebook = models.URLField(max_length=200, )
    twitter = models.URLField(max_length=200, )
    texto = models.TextField()
    imagen = models.ImageField(upload_to='media/Eventos/')
    linkUbicacion = models.CharField(max_length=200,default="")
    
    def __str__(self):
        return str(self.titulo)
    
    def __unicode__(self):
        return str(self.titulo)