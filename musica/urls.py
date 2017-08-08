from django.conf.urls import url

from . import views
from .views import DiscoView, DiscoCompletoView


urlpatterns = [
    url(r'^$', views.DiscoView, name=u'discos'),
    url(r'^(?P<nombDisco>[\w-]+)/$', DiscoCompletoView.as_view()),
]