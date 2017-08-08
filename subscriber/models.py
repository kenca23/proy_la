from django.db import models

# Create your models here.
class Subscriber(models.Model):
    nombre = models.CharField('Nombre',max_length=30,)
    email = models.EmailField('Correo Eléctronico',max_length=30,unique=True)
    pais = models.CharField('País',max_length=30 , blank=True)
    ciudad = models.CharField('Ciudad',max_length=30 , blank=True)
    
    def __str__(self):
        return str(self.nombre)
        
    def __unicode__(self):
        return str(self.nombre)