#encoding:utf-8
from django import forms
from apps.publico.models import Saludo

class SaludoForm(forms.ModelForm):
    class Meta:
    	fields = "__all__"
    	#fields = ['mensaje']
    	model = Saludo