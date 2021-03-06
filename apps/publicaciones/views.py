from django.shortcuts import render, get_object_or_404
from apps.publicaciones.models import Publicacion
from apps.general.views import get_contexto_general

def indexPublicaciones(request):
	contexto =  get_contexto_general(request)
	contexto['todas_las_publicaciones'] = Publicacion.objects.all().order_by('-fecha_publicacion')
	return render(request, 'publicaciones/publicaciones.html', contexto)

def detallesPublicacion(request, publicacion_tipo_publicacion, publicacion_titulo):
	contexto =  get_contexto_general(request)
	contexto['publicacion'] = get_object_or_404(Publicacion, titulo = publicacion_titulo)
	
	return render(request, 'publicaciones/publicacion.html', contexto)