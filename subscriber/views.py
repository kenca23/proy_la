from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .forms import SubscriberForm
from .models import Subscriber

# Create your views here.

def nuevo(request):
    if request.method == 'POST':
        form = SubscriberForm(data=request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            pais = form.cleaned_data['pais']
            ciudad = form.cleaned_data['ciudad']
            response_data = {}
    
            envio = Subscriber(nombre = nombre, email = email, pais = pais, ciudad = ciudad)
            envio.save()
    
            response_data['result'] = 'Muchas gracias por suscribirse a Lalalá!'
    
            return JsonResponse(response_data)
        else:
            return JsonResponse({'result' : "A ocurrido un error, verifique que los campos sean correctos."})
    else:
        return JsonResponse({'result' : "Error al enviar."})
    
    
    """if request.method == 'POST':
        form = SubscriberForm(data=request.POST)
        # check whether it's valid:
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            pais = form.cleaned_data['pais']
            ciudad = form.cleaned_data['ciudad']
            nuevo = Subscriber(nombre = nombre, email = email, pais = pais, ciudad = ciudad)
            result = nuevo.save()
            data = {
                'success': 'Muchas gracias por suscribirse a Lalalá'
            }
            return JsonResponse(data)"""
            
def validar_email(request):
    email = request.GET.get('email', None)
    data = {
        'is_taken': Subscriber.objects.filter(email__iexact=email).exists()
    }
    if data['is_taken']:
        data['error_message'] = email + ' ya está suscrito a Lalalá.'
    return JsonResponse(data)
    