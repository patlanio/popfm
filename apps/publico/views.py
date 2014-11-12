from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from apps.publico.models import Saludo
from apps.publico.forms import SaludoForm
from django.http import HttpResponseRedirect

def nuevo_saludo(request):
	if request.method == 'POST':
		formulario = SaludoForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = SaludoForm()

	return render_to_response('publico/complasenciaform.html', {'formulario': formulario}, context_instance = RequestContext(request))