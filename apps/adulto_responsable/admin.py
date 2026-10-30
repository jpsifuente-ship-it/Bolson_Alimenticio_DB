from django.contrib import admin
from .models import AdultoResponsable

@admin.register(AdultoResponsable)
class AdultoResponsableAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'dni')
    search_fields = ('nombre', 'dni')