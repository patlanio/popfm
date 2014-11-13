from django.db import models
import datetime

class Locutor(models.Model):
	nombre = models.CharField(max_length=128, verbose_name='Nombre completo', help_text='Nombre completo del locutor')
	foto = models.ImageField(upload_to='programas/locutores', help_text='Fotografia del locutor (De preferencia cuadrada en formato JPEG o JPG de 480 x 480 px minimo, si es mas pesada/grande las paginas tardaran demasiado en cargar)')
	miniatura = models.ImageField(upload_to='programas/locutores/miniaturas', help_text='Fotografia miniatura del locutor (De preferencia cuadrada en formato JPEG o JPG de 128 x 128 px maximo, si es mas pesada/grande las paginas tardaran demasiado en cargar)')
	descripcion = models.TextField(max_length=256, verbose_name='Descripcion del locutor', help_text='Proporcione una breve descripcion del locutor, maximo 256 caracteres')

	def __str__(self):
		return self.nombre

class Programa(models.Model):
	nombre = models.CharField(max_length=128)
	descripcion = models.TextField(max_length=256, verbose_name='Descripcion del programa', help_text='Indica la tematica tratada en el programa')
	imagen = models.ImageField(upload_to='programas/programa', help_text='Logo/Imagen representativo(a) del programa (De preferencia en formato JPEG o JPG de 768 x 432px, si es mas pesada/grande las paginas tardaran demasiado en cargar)')
	hora_inicio = models.TimeField(auto_now=False, verbose_name='Hora de inicio', help_text='Hora a la que inicia el programa')
	hora_fin = models.TimeField(auto_now=False, verbose_name='Hora a la que termina', help_text='Hora a la que finaliza el programa')
	locutores = models.ManyToManyField(Locutor, blank=True, help_text='Que locutores conducen este programa?')
	
	lunes = models.BooleanField(default=False, verbose_name='Se transmite el dia lunes?')
	martes = models.BooleanField(default=False, verbose_name='Se transmite el dia martes?')
	miercoles = models.BooleanField(default=False, verbose_name='Se transmite el dia miercoles?')
	jueves = models.BooleanField(default=False, verbose_name='Se transmite el dia jueves?')
	viernes = models.BooleanField(default=False, verbose_name='Se transmite el dia viernes?')
	sabado = models.BooleanField(default=False, verbose_name='Se transmite el dia sabado?')
	domingo = models.BooleanField(default=False, verbose_name='Se transmite el dia domingo?')

	activo = models.BooleanField(default=False, verbose_name='Esta activo?', help_text='Esta siendo transmitido actualmente al aire regularmente?')

	def __str__(self):
		return self.nombre