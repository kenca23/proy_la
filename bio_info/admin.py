from django.contrib import admin

# Register your models here.
from .models import Integrante, Banda

admin.site.register(Integrante)
admin.site.register(Banda)