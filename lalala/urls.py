"""lalala URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import home, Biografia, Prensa, Contacto, Gracias
from redireccion.views import LalalaRedirect
"""from musica.views import DiscoView, DiscoCompletoView
from eventos.views import Calendario, InfoEvento"""

"""urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name=u'home'),
    url(r'^discos/$', DiscoView, name=u'discos'),
    ---url(r'^discos/(?P<nombDisco>[\w-]+)/$', DiscoCompletoView.as_view()),
    url(r'^biografia/$', Biografia, name=u'biografia'),
    url(r'^calendario/$', Calendario, name=u'calendario'),
    ---url(r'^calendario/(?P<evento>[\w-]+)/$', InfoEvento.as_view()),
    url(r'^prensa/$', Prensa, name=u'prensa'),
    url(r'^contacto/$', Contacto, name=u'contacto'),
    url(r'^contacto/gracias-(?P<nombre>[\w\s]+)/$', Gracias.as_view()),
    url(r'^(?P<shortcode>[\w-]+)/$', LalalaRedirect.as_view()),
    
]"""

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name=u'home'),
    url(r'^discos/', include('musica.urls')),
    url(r'^biografia/$', Biografia, name=u'biografia'),
    url(r'^calendario/', include('eventos.urls')),
    url(r'^prensa/$', Prensa, name=u'prensa'),
    url(r'^contacto/$', Contacto, name=u'contacto'),
    url(r'^contacto/gracias-(?P<nombre>[\w\s]+)/$', Gracias.as_view()),
    url(r'^(?P<shortcode>[\w-]+)/$', LalalaRedirect.as_view()),
    url(r'^subscriptor/', include('subscriber.urls')),
    ]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
	urlpatterns += (static(settings.STATIC_URL, document_root= settings.STATIC_ROOT))