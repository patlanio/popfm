from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    ('', include('social.apps.django_app.urls', namespace='social')),
	(r'^admin/filebrowser/', include(site.urls)),
    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    (r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
)
