from django.shortcuts import render
import datetime
from django.db.models import Q


from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from smtplib import SMTP
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View


from musica.models import Disco, Video as videoHome
from eventos.models import Evento
from .forms import ContactForm, PrensaForm
from subscriber.forms import SubscriberForm
from shared.models import Imagen_Pagina
from bio_info.models import Banda, Miembro
from press_info.models import Foto, Video as videoPrensa, Press_Info, Enlace



def home(request):
    today = datetime.datetime.today()
    queryset = Disco.objects.all().order_by('-id')[:3]
    querysetEv = Evento.objects.filter(fecha__gte=datetime.datetime.today().date()).order_by('fecha')[0:6]
    videos = videoHome.objects.filter(fecha_salida__lte=datetime.datetime.today().date()).order_by('-fecha_salida')[0:5]
    kevin = Miembro.objects.filter(Q(fecha_salida__lte=today) & Q(nombre='Kevin Calvo')).order_by('-fecha_salida').first()
    kenneth = Miembro.objects.filter(Q(fecha_salida__lte=today) & Q(nombre='Kenneth Calvo')).order_by('-fecha_salida').first()
    bob = Miembro.objects.filter(Q(fecha_salida__lte=today) & Q(nombre='Roberto Cruz')).order_by('-fecha_salida').first()
    form = SubscriberForm
    imagen = Imagen_Pagina.objects.filter(Q(fecha__lte=today) & Q(nombre='SUB')).order_by('-fecha').first()
    urlImagen = imagen.imagen
    print(querysetEv)
    content = {
        'title' : 'Lalalá | Página Oficial',
        'titulo': 'Lalalá | Canción Actual',
        'object_list' : queryset,
        'evento' : querysetEv,
        'videos' : videos,
        'form' : form,
        'kevin' : kevin,
        'kenneth' : kenneth,
        'bob' : bob,
        'imagen' : urlImagen
    }
    print(queryset)
    return render(request, "home.html", content)  


def Biografia(request):
	today = datetime.datetime.today()
	imagen = Imagen_Pagina.objects.filter(Q(fecha__lte=today) & Q(nombre='BIO')).order_by('-fecha').first()
	banda = Banda.objects.filter(fecha_salida__lte=today).order_by('-fecha_salida').first()
	
	kevincalvo = Miembro.objects.filter(Q(fecha_salida__lte=today) & Q(nombre='Kevin Calvo')).order_by('-fecha_salida').first()
	kennethcalvo = Miembro.objects.filter(Q(fecha_salida__lte=today) & Q(nombre='Kenneth Calvo')).order_by('-fecha_salida').first()
	robertocruz = Miembro.objects.filter(Q(fecha_salida__lte=today) & Q(nombre='Roberto Cruz')).order_by('-fecha_salida').first()
	
	
	#integrantes = Integrante.objects.filter(fecha_salida__lte=today).order_by('fecha_salida').distinct()   #filter(Q(fecha__lte=today) & Q(nombre='BIO')).order_by('-fecha').first()
	print(banda)
	
	
	
	urlImagen = imagen.imagen
	content = {
	'title' : 'Lalalá | Página Oficial',
        'titulo': 'Biografía',
	'imagen' : urlImagen,
	'banda' : banda,
	'kevin' : kevincalvo,
	'kenneth' : kennethcalvo,
	'bob' : robertocruz,
	}
	return render(request, "biografia.html", content)  

def Prensa(request):
    form_class = PrensaForm
    
    if request.method == 'POST':
        form = form_class(data=request.POST)
        
        if form.is_valid():
            nombre = request.POST.get(
                'nombre', ''
            )
            email = request.POST.get(
                'email', ''
            )
            asunto = request.POST.get(
                'asunto', ''
            )
            content_texto = request.POST.get(
                'content', ''
            )
            
            enviar_a = 'manager@lalalaoficial.com'
            
            if nombre and email and enviar_a and asunto and content_texto:
                try:
                    correo = EmailMessage(
                        asunto,
                        content_texto,
                        nombre + '<' + email + '>',
                        [enviar_a],
                        headers = {'Reply-To': email }
                    )
                    correo.send()
                except BadHeaderError:
                    return HttpResponse('Datos invalidos.')
                
                argumentos = {
                    
                }
                return redirect('/contacto/gracias-'+nombre+'/')
                    
            
            #
    else:
    	today = datetime.datetime.today()
    	imagen = Imagen_Pagina.objects.filter(Q(fecha__lte=today) & Q(nombre='PRE')).order_by('-fecha').first()
    	kevincalvo = Miembro.objects.filter(Q(fecha_salida__lte=today) & Q(nombre='Kevin Calvo')).order_by('-fecha_salida').first()
    	kennethcalvo = Miembro.objects.filter(Q(fecha_salida__lte=today) & Q(nombre='Kenneth Calvo')).order_by('-fecha_salida').first()
    	robertocruz = Miembro.objects.filter(Q(fecha_salida__lte=today) & Q(nombre='Roberto Cruz')).order_by('-fecha_salida').first()
    	fotos = Foto.objects.filter(fecha_salida__lte=today).order_by('-fecha_salida') [0:15]
    	videosHome = videoHome.objects.filter(fecha_salida__lte=datetime.datetime.today().date()).order_by('-fecha_salida')[0:10]
    	videos = videoPrensa.objects.filter(fecha_salida__lte=today).order_by('-fecha_salida')[0:10]
    	
    	urlImagen = imagen.imagen
    	content = {
    	'title' : 'Lalalá | Página Oficial',
            'titulo': 'Prensa',
    	'imagen' : urlImagen,
    	'kevin' : kevincalvo,
    	'kenneth' : kennethcalvo,
    	'bob' : robertocruz,
    	'fotos': fotos,
    	'videoHome': videosHome,
    	'videos' : videos,
    	'form' : form_class,
    	}
    print(form_class)
    return render(request, "prensa.html", content) 

def Contacto(request):
    form_class = ContactForm
    
    if request.method == 'POST':
        form = form_class(data=request.POST)
        
        if form.is_valid():
            nombre = request.POST.get(
                'nombre', ''
            )
            email = request.POST.get(
                'email', ''
            )
            dirigido = request.POST.get(
                'dirigido', ''
            )
            asunto = request.POST.get(
                'asunto', ''
            )
            content_texto = request.POST.get(
                'content', ''
            )
            
            if dirigido == 'Kenneth Calvo':
                enviar_a = 'kenneth.calvo@lalalaoficial.com'
            elif dirigido == 'Kevin Calvo':
                enviar_a = 'kevin.calvo@lalalaoficial.com'
            else:
                enviar_a = 'kenneth.calvo@lalalaoficial.com'
                
                
            if nombre and email and enviar_a and asunto and content_texto:
                try:
                    correo = EmailMessage(
                        asunto,
                        content_texto,
                        nombre + '<' + email + '>',
                        [enviar_a],
                        headers = {'Reply-To': email }
                    )
                    correo.send()
                except BadHeaderError:
                    return HttpResponse('Datos invalidos.')
                
                argumentos = {
                    
                }
                return redirect('/contacto/gracias-'+nombre+'/')
                    
            
            #
    else:
        today = datetime.datetime.today()
        imagen = Imagen_Pagina.objects.filter(Q(fecha__lte=today) & Q(nombre='CON')).order_by('-fecha').first()
        
        urlImagen = imagen.imagen
        content = {
            'title' : 'Lalalá | Contacto',
            'titulo': 'Contacto',
            'form' : form_class,
            'imagen' : urlImagen
        }
        
    print(form_class)
    return render(request, "contacto.html", content)  


class Gracias(View):
    def get(self, request,nombre=None, *args, **kwargs):
        today = datetime.datetime.today()
        imagen = Imagen_Pagina.objects.filter(Q(fecha__lte=today) & Q(nombre='GRA')).order_by('-fecha').first()
        
        urlImagen = imagen.imagen
        print(nombre)
        content = {
            'title' : 'Gracias',
            'titulo': 'Gracias, ' + nombre,
            'nombre' : nombre,
            'imagen' : urlImagen
        }
        
        return render(request, "gracias.html", content)  
