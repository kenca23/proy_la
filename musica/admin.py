from django.contrib import admin

# Register your models here.

from .models import Disco, Cancion, Ficha_Tecnica, Disponible_En_Disco, Video, SmartLink, Link_SmartLink #, Sencillo, Ficha_Tecnica_Sencillo, Disponible_En_Sencillo

admin.site.register(Disco)
admin.site.register(Cancion)
admin.site.register(Ficha_Tecnica)
admin.site.register(Disponible_En_Disco)
admin.site.register(Video)
admin.site.register(SmartLink)
admin.site.register(Link_SmartLink)
#admin.site.register(Sencillo)
#admin.site.register(Ficha_Tecnica_Sencillo)
#admin.site.register(Disponible_En_Sencillo)
