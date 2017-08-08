from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
import datetime

# Import Tabla Disco de la base de datos
from .models import Evento

class InfoEvento(View):
    def get(self, request, evento=None, *args, **kwargs):
        eventoI = Evento.objects.get(linkEvento=evento)
        content = {
            'title' : 'Lalalá | {sc}'.format(sc=eventoI.titulo),
            'titulo': '{sc}'.format(sc=eventoI.titulo),
            'object_list' : eventoI,
        }
        return render(request, "infoEvento.html", content)  
		

def Calendario(request):
    queryset = Evento.objects.filter(fecha__gte=datetime.datetime.today().date()).order_by('fecha')
    content = {
        'title' : 'Lalalá | Calendario',
        'titulo': 'Calendario',
        'object_list' : queryset,
    }
    print(queryset)
    return render(request, "calendario.html", content)  


    
