from django.urls import path

from apps.trabajador_s.views import (
    TrabajadorSocialCreateView,
    TrabajadorSocialDeleteView,
    TrabajadorSocialDetailView,
    TrabajadorSocialListView,
    TrabajadorSocialUpdateView,
)

app_name = 'trabajador_s'

urlpatterns = [
    path('', TrabajadorSocialListView.as_view(), name='list'),
    path('create/', TrabajadorSocialCreateView.as_view(), name='create'),
    path('update/<int:pk>/', TrabajadorSocialUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', TrabajadorSocialDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>/', TrabajadorSocialDetailView.as_view(), name='detail'),
]
