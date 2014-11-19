from django.contrib import admin
from apps.publico.models import Saludo


class SaludoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'id', 'leido', 'fecha_creacion', 'correo',)
	list_filter = ['leido','fecha_creacion']
	search_fields = ['nombre',]
	ordering = ['leido', '-fecha_creacion' ]

admin.site.register(Saludo, SaludoAdmin)