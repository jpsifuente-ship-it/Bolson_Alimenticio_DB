from django.urls import path

from apps.estudiante.views import (
    EstudianteCreateView,
    EstudianteDeleteView,
    EstudianteDetailView,
    EstudianteListView,
    EstudianteUpdateView,
)

app_name = 'estudiante'

urlpatterns = [
    path('', EstudianteListView.as_view(), name='list'),
    path('create/', EstudianteCreateView.as_view(), name='create'),
    path('update/<int:pk>/', EstudianteUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', EstudianteDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>/', EstudianteDetailView.as_view(), name='detail'),
]
