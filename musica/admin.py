from django.contrib import admin

# Register your models here.

from .models import Disco, Cancion, Ficha_Tecnica

admin.site.register(Disco)
admin.site.register(Cancion)
admin.site.register(Ficha_Tecnica)
