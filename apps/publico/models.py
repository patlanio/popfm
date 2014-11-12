from django.db import models

class Saludo(models.Model):
	autor = models.CharField(max_length=32, verbose_name='Como te llamas?')
	email = models.EmailField(verbose_name='Cual es tu correo?')
	mensaje = models.TextField(max_length=200)
	fecha_creacion = models.DateTimeField(auto_now_add = True)
	leido = models.BooleanField(default = False, verbose_name='Marcar como leido', help_text='Marcar este mensaje como leido cuando se haya hecho la mencion al aire')

	def __str__(self):
		return self.autor + " - " + self.email