from django.contrib import admin
from .models import Retiro

@admin.register(Retiro)
class RetiroAdmin(admin.ModelAdmin):
    list_display = ('id', 'estudiante', 'adulto', 'fecha_retiro')
    search_fields = ('estudiante__nombre', 'adulto__nombre')