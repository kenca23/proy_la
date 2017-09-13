from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.db.models import Q

# Import Tabla Disco de la base de datos
from .models import Evento
from shared.models import Imagen_Pagina

class InfoEvento(View):
    def get(self, request, evento=None, *args, **kwargs):
        eventoI = Evento.objects.get(linkEvento=evento)
        today = datetime.datetime.today()
        imagen = Imagen_Pagina.objects.filter(Q(fecha__lte=today) & Q(nombre='GRA')).order_by('-fecha').first()
        
        urlImagen = imagen.imagen
        content = {
            'title' : 'Lalalá | {sc}'.format(sc=eventoI.titulo),
            'titulo': '{sc}'.format(sc=eventoI.titulo),
            'evento' : eventoI,
            'imagen' : urlImagen,
        }
        return render(request, "infoEvento.html", content)  
		

def Calendario(request):
    queryset = Evento.objects.filter(fecha__gte=datetime.datetime.today().date()).order_by('fecha')
    today = datetime.datetime.today()
    imagen = Imagen_Pagina.objects.filter(Q(fecha__lte=today) & Q(nombre='GRA')).order_by('-fecha').first()
    
    urlImagen = imagen.imagen
    content = {
        'title' : 'Lalalá | Calendario',
        'titulo': 'Calendario',
        'object_list' : queryset,
        'imagen' : urlImagen,
    }
    print(queryset)
    return render(request, "calendario.html", content)  


    
