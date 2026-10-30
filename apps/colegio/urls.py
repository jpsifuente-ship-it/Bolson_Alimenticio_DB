from django.urls import path

from apps.colegio.views import (
    ColegioCreateView,
    ColegioDeleteView,
    ColegioDetailView,
    ColegioListView,
    ColegioUpdateView,
)

app_name = 'colegio'

urlpatterns = [
    path('', ColegioListView.as_view(), name='list'),
    path('create/', ColegioCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ColegioUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ColegioDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>/', ColegioDetailView.as_view(), name='detail'),
]
