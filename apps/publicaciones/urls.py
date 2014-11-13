from django.conf.urls import patterns, url
from apps.publicaciones import views

urlpatterns = patterns('',
	url(r'^publicaciones/$', views.indexPublicaciones, name='index'),
	url(r'^(?P<publicacion_tipo_publicacion>.+)/(?P<publicacion_titulo>.+)/$', views.detallesPublicacion, name='publicacion'),
)