from django.conf.urls import patterns, url
from apps.eventos import views

urlpatterns = patterns('',
	url(r'^eventos/$', views.indexEventos, name='indexEventos'),
	url(r'^evento/(?P<evento_nombre>.+)/$', views.detallesEvento, name='evento'),
)