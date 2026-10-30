from django.urls import path

from apps.punto_de_entrega.views import (
    PuntoDeEntregaCreateView,
    PuntoDeEntregaDeleteView,
    PuntoDeEntregaDetailView,
    PuntoDeEntregaListView,
    PuntoDeEntregaUpdateView,
)

app_name = 'punto_de_entrega'

urlpatterns = [
    path('', PuntoDeEntregaListView.as_view(), name='list'),
    path('create/', PuntoDeEntregaCreateView.as_view(), name='create'),
    path('update/<int:pk>/', PuntoDeEntregaUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', PuntoDeEntregaDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>/', PuntoDeEntregaDetailView.as_view(), name='detail'),
]
