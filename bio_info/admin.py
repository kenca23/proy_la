from django.contrib import admin

# Register your models here.
from .models import Miembro, Banda

admin.site.register(Miembro)
admin.site.register(Banda)