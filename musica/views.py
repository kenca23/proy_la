from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect

# Import Tabla Disco de la base de datos
from .models import Disco, Cancion, Ficha_Tecnica

class DiscoCompletoView(View):
    def get(self, request, nombDisco=None, *args, **kwargs):
        disco = get_object_or_404(Disco, nombDisco=nombDisco)
        canciones = Cancion.objects.filter(disco=disco.id).order_by('numero')
        ficha_tecnica = Ficha_Tecnica.objects.filter(disco=disco.id)
        
        nombreDisco = disco.nombre
        content = {
            'title' : 'Lalalá | {sc}'.format(sc=nombreDisco),
            'titulo': '{sc}'.format(sc=nombreDisco),
            'disco' : disco,
            'canciones' : canciones,
            'fichas_tecnicas' : ficha_tecnica
        }
        return render(request, "discoCompleto.html", content)  
		

def DiscoView(request):
    queryset = Disco.objects.all().order_by('-anno')
    content = {
        'title' : 'Lalalá | Discografía',
        'titulo': 'Discografía',
        'object_list' : queryset,
    }
    return render(request, "discografia.html", content)  


    
