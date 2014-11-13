from django.shortcuts import render, get_object_or_404
from apps.eventos.models import Evento, Imagen, Video
from apps.general.views import get_contexto_general

def indexEventos(request):
	contexto =  get_contexto_general(request)
	contexto['eventos'] = Evento.objects.all().order_by('-fecha_creacion')
	
	return render(request, 'eventos/eventos.html', contexto)

def detallesEvento(request, evento_nombre):
	contexto =  get_contexto_general(request)
	evento = get_object_or_404(Evento, nombre = evento_nombre)
	contexto['evento'] = evento
	contexto['imagenes_evento'] = Imagen.objects.filter(evento = evento.id)
	contexto['videos_evento'] = Video.objects.filter(evento = evento.id)
	
	return render(request, 'eventos/evento.html', contexto)

def indexVideos(request):
	contexto =  get_contexto_general(request)
	contexto['videos'] = Video.objects.all().order_by('-fecha_subida')
	
	return render(request, 'eventos/videos.html', contexto)