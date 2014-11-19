#encoding:utf-8
from django.db import models

class Saludo(models.Model):
	nombre = models.CharField(max_length=64)
	correo = models.EmailField(verbose_name='Correo')
	mensaje = models.TextField(max_length=200)
	fecha_creacion = models.DateTimeField(auto_now_add = True)
	leido = models.BooleanField(default = False, help_text='Marcar este mensaje como leido cuando se haya hecho la mencion al aire')

	def __str__(self):
		return self.correo