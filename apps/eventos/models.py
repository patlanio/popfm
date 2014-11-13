#encoding:utf-8
from django.db import models
from tinymce.models import HTMLField

class Evento(models.Model):
	nombre = models.CharField(max_length=128)
	imagen_principal = models.ImageField(upload_to="eventos/imagenes_principales", verbose_name='Imagen distintiva', help_text='Imagen que hace referencia al evento, donde paso, quienes fueron, cuando, etc. (De preferencia en formato JPEG o JPG de 1366 x 768 px, si es mas pesada/grande las paginas tardaran demasiado en cargar)')
	parrafo_principal = models.TextField(max_length=250, help_text='Pequeña descripcion precisa y corta (maximo 250 caracteres), aparecera como el texto de enganche para los usuarios')
	cuerpo = HTMLField(help_text='Cuerpo principal de la entrada')
	fecha_creacion = models.DateTimeField(auto_now_add = True)
	fecha_evento = models.DateTimeField(verbose_name='Fecha del evento')

	def __str__(self):
		return self.nombre

class Imagen(models.Model):
	evento = models.ForeignKey(Evento, help_text='A que evento pertenece?')
	imagen = models.ImageField(upload_to = "eventos/imagenes", help_text='De preferencia en formato JPEG o JPG de 1366 x 768 px, si es mas pesada/grande las paginas tardaran demasiado en cargar')
	fecha_subida = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return 'IMG_'+ str(self.id) +' '+ self.evento.nombre

class Video(models.Model):
	evento = models.ForeignKey(Evento, blank=True, null=True, help_text='A que evento pertenece?')
	url = models.URLField(max_length=200, verbose_name='Enlace de Youtube', help_text='Enlace al video alojado en Youtube; similar a este: [Ir al video, hacer click en compartir, despues en insertar video y copiar el enlace; es similar a esta: www.youtube.com/embed/iS1g8G_njx8 ] ')
	fecha_subida = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return 'VID_'+ str(self.id) +' '+ self.evento.nombre