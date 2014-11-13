from django.contrib import admin
from apps.eventos.models import Evento, Imagen, Video

class ImagenInline(admin.TabularInline):
	model = Imagen
	extra = 3

class VideoInline(admin.TabularInline):
	model = Video
	extra = 1

class EventoAdmin(admin.ModelAdmin):
	inlines = [ImagenInline, VideoInline]

admin.site.register(Evento, EventoAdmin)
admin.site.register(Imagen)
admin.site.register(Video)
