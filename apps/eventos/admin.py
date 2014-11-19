from django.contrib import admin
from apps.eventos.models import Evento, Imagen, Video

class ImagenAdmin(admin.ModelAdmin):
	ordering = ['-fecha_subida']
	list_display = ('id', 'evento', 'fecha_subida')
	list_filter = ['evento', 'fecha_subida']

class ImagenInline(admin.TabularInline):
	model = Imagen
	extra = 3

class VideoAdmin(admin.ModelAdmin):
	ordering = ['-fecha_subida']
	list_display = ('id', 'evento', 'fecha_subida')
	list_filter = ['evento', 'fecha_subida']

class VideoInline(admin.TabularInline):
	model = Video
	extra = 1

class EventoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'id', 'fecha_evento', 'fecha_creacion')
	list_filter = ['fecha_evento', 'fecha_creacion']
	inlines = [ImagenInline, VideoInline]
	search_fields = ['nombre']
	ordering = ['-fecha_evento',]

admin.site.register(Evento, EventoAdmin)
admin.site.register(Imagen, ImagenAdmin)
admin.site.register(Video, VideoAdmin)