from django.conf.urls import patterns, url
from apps.programas import views

urlpatterns = patterns('',
	url(r'^programas/$', views.indexProgramas, name='programas'),
	url(r'^programa/(?P<programa_nombre>.+)/$', views.detallesPrograma, name='programa'),
)