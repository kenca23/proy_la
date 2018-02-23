from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
import datetime

# Import Tabla Disco de la base de datos
from shared.models import Imagen_Pagina
from .models import Disco, Cancion, Ficha_Tecnica, Disponible_En_Disco, SmartLink, Link_SmartLink #Sencillo, Ficha_Tecnica_Sencillo, Disponible_En_Sencillo

class DiscoCompletoView(View):
    def get(self, request, nombDisco=None, *args, **kwargs):
        disco = get_object_or_404(Disco, nombDisco=nombDisco)
        canciones = Cancion.objects.filter(disco=disco.id).order_by('numero')
        ficha_tecnica = Ficha_Tecnica.objects.filter(disco=disco.id)
        disponible_en = Disponible_En_Disco.objects.filter(disco=disco.id)
        
        nombreDisco = disco.nombre
        urlImagen = disco.imagen_grande
        content = {
            'title' : 'Lalalá | {sc}'.format(sc=nombreDisco),
            'titulo': '{sc}'.format(sc=nombreDisco),
            'disco' : disco,
            'canciones' : canciones,
            'fichas_tecnicas' : ficha_tecnica,
            'imagen' : urlImagen,
            'disponible_en' : disponible_en
        }
        return render(request, "discoCompleto.html", content)  
		
class SmartLinkView(View):
    def get(self, request, nombSmart=None, *args, **kwargs):
        smartlink = get_object_or_404(SmartLink, nombSmart=nombSmart)
        links = Link_SmartLink.objects.filter(smartlink=smartlink.id)
        
        nombreSmart = smartlink.nombre
        content = {
            'title' : 'Lalalá | {sc}'.format(sc=nombreSmart),
            'titulo': '{sc}'.format(sc=nombreSmart),
            'smartlink' : smartlink,
            'links' : links,
        }
        return render(request, "smartlink.html", content)  


#def DiscoView(request):
#    queryset = Disco.objects.all().order_by('-anno')
#    today = datetime.datetime.today()
#    imagen = Imagen_Pagina.objects.filter(Q(fecha__lte=today) & Q(nombre='DIS')).order_by('-fecha').first()
    
#    urlImagen = imagen.imagen
#    content = {
#        'title' : 'Lalalá | Discografía',
#        'titulo': 'Discografía',
#        'object_list' : queryset,
#        'imagen' : urlImagen,
#    }
#    return render(request, "discografia.html", content)  
    
    
    
def DiscoView(request):
    today = datetime.datetime.today()
    queryset = Disco.objects.filter(Q(fecha_salida__lte=today)).order_by('-anno')
    
    #sencillos = Sencillo.objects.filter(Q(fecha_salida__lte=today)).order_by('-fecha_salida').prefetch_related('disponible_en_sencillo_set').prefetch_related('ficha_tecnica_sencillo_set')
    #print(sencillos.values())
    #print("\n\n")
    
    imagen = Imagen_Pagina.objects.filter(Q(fecha__lte=today) & Q(nombre='DIS')).order_by('-fecha').first()
    
    urlImagen = imagen.imagen
    content = {
        'title' : 'Lalalá | Música',
        'titulo': 'Música',
        'object_list' : queryset,
        'imagen' : urlImagen,
    }
    return render(request, "discografia.html", content) 


    
