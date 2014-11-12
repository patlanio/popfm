from django.contrib import admin
from apps.publicaciones.models import Publicacion, Categoria

class PublicacionAdmin(admin.ModelAdmin):
	# fieldsets = [
	# 	(None,               {'fields': ['titulo']}),
	# 	('Date information', {'fields': ['fecha_publicacion'], 'classes': ['collapse']}),
	# ]

	list_display = ('titulo', 'id', 'en_portada', 'listo_para_publicar', 'tipo_publicacion', 'fecha_publicacion', 'fecha_expiracion', 'fecha_creacion')
	list_filter = ['en_portada', 'listo_para_publicar', 'tipo_publicacion', 'fecha_publicacion', 'fecha_expiracion', 'fecha_creacion']
	search_fields = ['titulo']
	ordering = ['-fecha_publicacion',]
	#date_hierarchy = ['fecha_publicacion',] #no puedo hacerlo funcionar
	
admin.site.register(Publicacion, PublicacionAdmin)
admin.site.register(Categoria)