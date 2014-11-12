from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views import generic
from apps.publicaciones.models import Publicacion
#from apps.programas.models import Programa
from apps.publico.models import Saludo
from apps.publico.forms import SaludoForm
from django.http import HttpResponseRedirect
from apps.general.views import get_contexto_general

def indexPublicaciones(request):
	contexto =  get_contexto_general(request)
	contexto['todas_las_publicaciones'] = Publicacion.objects.all().order_by('-fecha_publicacion')
	return render(request, 'publicaciones/publicaciones.html', contexto)

def detallesPublicacion(request, publicacion_id):
	publicacion = get_object_or_404(Publicacion, pk = publicacion_id)

	if request.method == 'POST':
		formulario = SaludoForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/publicaciones')
	else:
		formulario = SaludoForm()


	contexto = {'programa_al_aire':programa_al_aire,'formulario':formulario, 'saludos':saludos, 'publicacion':publicacion}
	
	return render(request, 'publicaciones/publicacion.html', contexto)