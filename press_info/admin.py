from django.contrib import admin

# Register your models here.
from .models import Press_Info, Foto, Video, Enlace

admin.site.register(Press_Info)
admin.site.register(Foto)
admin.site.register(Video)
admin.site.register(Enlace)