from django.contrib import admin

# Register your models here.
from .models import Press_Info, Integrante, Foto, Video, Enlace

admin.site.register(Press_Info)
admin.site.register(Integrante)
admin.site.register(Foto)
admin.site.register(Video)
admin.site.register(Enlace)