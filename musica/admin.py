from django.contrib import admin

# Register your models here.

from .models import Disco, Cancion, Ficha_Tecnica, Disponible_En_Disco, Video#, Sencillo, Ficha_Tecnica_Sencillo, Disponible_En_Sencillo

admin.site.register(Disco)
admin.site.register(Cancion)
admin.site.register(Ficha_Tecnica)
admin.site.register(Disponible_En_Disco)
admin.site.register(Video)
#admin.site.register(Sencillo)
#admin.site.register(Ficha_Tecnica_Sencillo)
#admin.site.register(Disponible_En_Sencillo)
