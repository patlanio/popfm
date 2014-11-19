from django.contrib import admin
from apps.programas.models import Programa, Locutor

class LocutorAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'id',)
	search_fields = ['nombre']
	ordering = ['nombre',]

class ProgramaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'id', 'hora_inicio', 'hora_fin', 'lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo')
	list_filter = ['hora_inicio', 'hora_fin']
	search_fields = ['nombre']
	ordering = ['hora_inicio',]

admin.site.register(Programa, ProgramaAdmin)
admin.site.register(Locutor, LocutorAdmin)