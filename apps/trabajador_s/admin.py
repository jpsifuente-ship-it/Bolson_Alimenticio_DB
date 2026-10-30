from django.contrib import admin
from .models import TrabajadorSocial

@admin.register(TrabajadorSocial)
class TrabajadorSocialAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'correo_electronico')
    search_fields = ('nombre', 'apellido', 'correo_electronico')