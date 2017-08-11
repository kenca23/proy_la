from django.db import models

class Imagen_Pagina(models.Model):
    DISCOGRAFIA = 'DIS'
    CALENDARIO = 'CAL'
    BIOGRAFIA = 'BIO'
    PRENSA = 'PRE'
    CONTACTO = 'CON'
    GRACIAS = 'GRA'
    
    PAGINA = (
        (DISCOGRAFIA, 'Discografía'),
        (CALENDARIO, 'Calendario'),
        (BIOGRAFIA, 'Biografía'),
        (PRENSA, 'Prensa'),
        (CONTACTO, 'Contacto'),
        (GRACIAS, 'Gracias'),
    )
    nombre = models.CharField(
        max_length=3,
        choices=PAGINA,
        default=DISCOGRAFIA,
    )
    imagen = models.ImageField(upload_to='media/imagen_paginas/')
    fecha = models.DateField()
    
    def __str__(self):
        return str(self.nombre + ' : ' + self.fecha.strftime("%d/%m/%y"))

    def __unicode__(self):
        return str(self.nombre + ' : ' + self.fecha.strftime("%d/%m/%y"))