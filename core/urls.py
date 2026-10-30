from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='inicio.html'), name='inicio'),
    path('security/', include('apps.security.urls')),
    path('colegio/', include('apps.colegio.urls')),
    path('estudiante/', include('apps.estudiante.urls')),
    path('adulto_responsable/', include('apps.adulto_responsable.urls')),
    path('punto_de_entrega/', include('apps.punto_de_entrega.urls')),
    path('retiro/', include('apps.retiro.urls')),
    path('trabajador_s/', include('apps.trabajador_s.urls')),
]
