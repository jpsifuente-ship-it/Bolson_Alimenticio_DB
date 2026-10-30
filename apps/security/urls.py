from django.urls import path

from apps.security.views import SecurityLoginView, SecurityLogoutView

app_name = 'security'

urlpatterns = [
    path('login/', SecurityLoginView.as_view(), name='login'),
    path('logout/', SecurityLogoutView.as_view(), name='logout'),
]
