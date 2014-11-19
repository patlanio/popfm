from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.utils import timezone
from apps.publicaciones.models import Publicacion
from django.http import HttpResponseRedirect
def logOut(request):
	logout(request)
	return redirect('/')

def index(request):
	contexto = get_contexto_general(request)
	#contexto['publicaciones_en_portada'] =  Publicacion.objects.filter(fecha_expiracion__gte=timezone.now()).filter(fecha_publicacion__lte = timezone.now()).filter(listo_para_publicar = True).filter(en_portada = True).order_by('fecha_publicacion')[:12]
	contexto['publicaciones_en_portada'] =  Publicacion.objects.filter(fecha_expiracion__gte=timezone.now()).filter(listo_para_publicar = True).filter(en_portada = True).order_by('-fecha_publicacion')[:12]
	contexto['ultimas_publicaciones'] = Publicacion.objects.filter(listo_para_publicar = True).order_by('-fecha_publicacion')[:12]
	
	return render(request, 'general/pagina_principal.html', contexto)

def get_contexto_general(request):
	#from apps.programas.models import Programa
	from apps.publico.models import Saludo
	from apps.publico.forms import SaludoForm
	saludos = Saludo.objects.all()
	#programa_al_aire = Programa.objects.filter(hora_fin__lte=timezone.now()).order_by('-hora_fin')[:1]

	if request.method == 'POST':
		formulario = SaludoForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = SaludoForm()
	
	#contexto_general = {'programa_al_aire':programa_al_aire,'formulario':formulario, 'saludos':saludos}
	contexto_general = {'formulario':formulario, 'saludos':saludos}
	return contexto_general