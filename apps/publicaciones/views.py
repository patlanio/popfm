from django.shortcuts import render, get_object_or_404

from django.utils import timezone
from django.views import generic
from apps.publicaciones.models import Publicacion
from apps.programas.models import Programa
from apps.publico.models import Saludo
from apps.publico.forms import SaludoForm
from django.http import HttpResponseRedirect

saludos = Saludo.objects.all()
programa_al_aire = Programa.objects.filter(hora_fin__lte=timezone.now()).order_by('-hora_fin')[:1]

def indexPublicaciones(request):
	todas_las_publicaciones = Publicacion.objects.all().order_by('-fecha_publicacion')

	if request.method == 'POST':
		formulario = SaludoForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/publicaciones')
	else:
		formulario = SaludoForm()

	
	contexto = {'programa_al_aire':programa_al_aire,'formulario':formulario, 'saludos':saludos, 'todas_las_publicaciones':todas_las_publicaciones}
	
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