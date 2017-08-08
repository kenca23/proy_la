from django.shortcuts import render
import datetime


from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from smtplib import SMTP
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View


from musica.models import Disco
from eventos.models import Evento
from .forms import ContactForm
from subscriber.forms import SubscriberForm

def home(request):
    queryset = Disco.objects.all().order_by('-id')[:3]
    querysetEv = Evento.objects.filter(fecha__gte=datetime.datetime.today().date()).order_by('fecha')[0:6]
    form = SubscriberForm
    print(querysetEv)
    content = {
        'title' : 'Lalalá | Página Oficial',
        'titulo': 'Lalalá | Canción Actual',
        'object_list' : queryset,
        'evento' : querysetEv,
        'form' : form
    }
    print(queryset)
    return render(request, "home.html", content)  


def Biografia(request):
	queryset = Disco.objects.all().order_by('-id')[:1]
	querysetEv = Evento.objects.filter(fecha__gte=datetime.datetime.today().date()).order_by('fecha')[:6]
	content = {
	'title' : 'Lalalá | Página Oficial',
        'titulo': 'Biografía',
	'object_list' : queryset,
	'evento' : querysetEv
	}
	print(queryset)
	return render(request, "biografia.html", content)  

def Prensa(request):
	queryset = Disco.objects.all().order_by('-id')[:1]
	querysetEv = Evento.objects.filter(fecha__gte=datetime.datetime.today().date()).order_by('fecha')[:6]
	content = {
	'title' : 'Lalalá | Página Oficial',
        'titulo': 'Prensa',
	'object_list' : queryset,
	'evento' : querysetEv
	}
	print(queryset)
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
        content = {
            'title' : 'Lalalá | Contacto',
            'titulo': 'Contacto',
            'form' : form_class
        }
        
    print(form_class)
    return render(request, "contacto.html", content)  


class Gracias(View):
    def get(self, request,nombre=None, *args, **kwargs):
        print(nombre)
        content = {
            'title' : 'Gracias',
            'titulo': 'Gracias, ' + nombre,
            'nombre' : nombre
        }
        
        return render(request, "gracias.html", content)  
