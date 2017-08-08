from django.conf.urls import url

from . import views
from .views import Calendario, InfoEvento
urlpatterns = [
    url(r'^$', views.Calendario, name=u'calendario'),
    url(r'^(?P<evento>[\w-]+)/$', InfoEvento.as_view()),
]