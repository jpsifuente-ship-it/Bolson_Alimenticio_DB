from django.urls import path

from apps.retiro.views import (
    RetiroCreateView,
    RetiroDeleteView,
    RetiroDetailView,
    RetiroListView,
    RetiroUpdateView,
)

app_name = 'retiro'

urlpatterns = [
    path('', RetiroListView.as_view(), name='list'),
    path('create/', RetiroCreateView.as_view(), name='create'),
    path('update/<int:pk>/', RetiroUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', RetiroDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>/', RetiroDetailView.as_view(), name='detail'),
]
