from django.conf.urls import url

from . import views

app_name='subscribers'
urlpatterns = [
    url(r'^ajax/nuevo/$', views.nuevo, name='nuevo'),
    url(r'^ajax/validar_email/$', views.validar_email, name='validar_email')
]