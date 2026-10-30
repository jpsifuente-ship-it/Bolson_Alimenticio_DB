from django.urls import path

from apps.adulto_responsable.views import (
    AdultoResponsableCreateView,
    AdultoResponsableDeleteView,
    AdultoResponsableDetailView,
    AdultoResponsableListView,
    AdultoResponsableUpdateView,
)

app_name = 'adulto_responsable'

urlpatterns = [
    path('', AdultoResponsableListView.as_view(), name='list'),
    path('create/', AdultoResponsableCreateView.as_view(), name='create'),
    path('update/<int:pk>/', AdultoResponsableUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', AdultoResponsableDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>/', AdultoResponsableDetailView.as_view(), name='detail'),
]
