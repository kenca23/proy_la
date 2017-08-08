from django.conf import settings
from django.db import models

# Create your models here.

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 50)

class redireccionamiento (models.Model):
	nombre 		= models.CharField(max_length=100, )
	url 		= models.CharField(max_length=220, )
	shortcode 	= models.CharField(max_length=SHORTCODE_MAX, unique=True )
	fecha		= models.DateTimeField(auto_now=False, auto_now_add=False)

	def __str__(self):
		return str(self.nombre)

	def __unicode__(self):
		return str(self.nombre)





'''
python manage.py makemigrations
python manage.py migrate
'''