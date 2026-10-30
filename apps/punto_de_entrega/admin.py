from django.contrib import admin
from .models import ConfirmacionDeRetiro

@admin.register(ConfirmacionDeRetiro)
class ConfirmacionDeRetiroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)
