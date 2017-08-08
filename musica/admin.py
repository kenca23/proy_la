from django.contrib import admin

# Register your models here.

from .models import Disco, Cancion

admin.site.register(Disco)
admin.site.register(Cancion)
