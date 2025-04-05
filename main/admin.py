from django.contrib import admin
from .models import Consulta

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'fecha_consulta')
    search_fields = ('nombre', 'email')
    list_filter = ('fecha_consulta',)
