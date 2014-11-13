from django.shortcuts import render, get_object_or_404
from apps.programas.models import Programa
from apps.general.views import get_contexto_general

def indexProgramas(request):
	contexto = get_contexto_general(request)
	contexto['programas'] = Programa.objects.filter(activo = True).order_by('hora_inicio')
	
	return render(request, 'programas/programas.html', contexto)

def detallesPrograma(request, programa_nombre):
	contexto = get_contexto_general(request)
	contexto['programa'] = get_object_or_404(Programa, nombre = programa_nombre)
	
	return render(request, 'programas/programa.html', contexto)