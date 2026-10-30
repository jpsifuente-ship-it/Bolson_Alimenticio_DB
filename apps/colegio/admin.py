from django.contrib import admin
from .models import Colegio

@admin.register(Colegio)
class ColegioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'direccion', 'correo_electronico', 'numero_telefono')
    search_fields = ('nombre', 'direccion', 'correo_electronico', 'numero_telefono')
