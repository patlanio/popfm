from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from filebrowser.sites import site

admin.autodiscover()

urlpatterns = patterns('',
    ('', include('social.apps.django_app.urls', namespace='social')),
	(r'^admin/filebrowser/', include(site.urls)),
    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    (r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
    
    url(r'^$', 'apps.general.views.index', name='index'),
    url(r'^salir/$', 'apps.general.views.logOut'),
    url(r'^', include('apps.publicaciones.urls', namespace="publicaciones")),
    url(r'^', include('apps.programas.urls', namespace="programas")),
    url(r'^', include('apps.eventos.urls', namespace="eventos")),
)
