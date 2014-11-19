#encoding:utf-8
from django.db import models

from tinymce.models import HTMLField
import datetime

class Categoria(models.Model):
	nombre = models.CharField(max_length=16, verbose_name='Nombre de la categoria', help_text='Poner el nombre en minusculas y en singular [se usa para poner en la URL, por ejemplo /chisme, /noticia, /tip, etc] ')

	def __str__(self):
		return self.nombre

class Publicacion(models.Model):
	titulo = models.CharField(max_length=48, help_text='Titulo de la publicacion, maximo 48 caracteres')
	imagen = models.ImageField(upload_to='publicaciones/portadas', verbose_name='Imagen principal', help_text='Da a entender el tipo contenido de la publicacion. Esta aparecera en la pagina principal del sitio si se marca la opcion -En portada- ')
	parrafo_principal = models.TextField(max_length=250, help_text='Debe ser preciso y corto (maximo 250 caracteres), aparecera como el texto de enganche para los usuarios')
	cuerpo = HTMLField(help_text='Cuerpo principal de la entrada')
	#tipo_publicacion = models.CharField(max_length=15, choices=TIPOS_DE_PUBLICACION, default="publicacion")
	tipo_publicacion = models.ForeignKey(Categoria)
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	fecha_publicacion = models.DateTimeField('Fecha de publicacion', help_text='Indica la fecha en la cual la publicacion aparecera automaticamente [Tambien debe estar marcada la opcion "Listo para publicar para que sea valido"]')
	fecha_expiracion = models.DateTimeField('Fecha de expiracion', help_text='Fecha de vence la promocion/publicacion')
	
	en_portada = models.BooleanField(default=False, help_text='Debe aparecer en la pagina principal del sitio?')
	listo_para_publicar = models.BooleanField(default=False, help_text='Hasta que no este marcada esta opcion nunca se mostrara esta publicacion')
	
	def __str__(self):
		return self.titulo