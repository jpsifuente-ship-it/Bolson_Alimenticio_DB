from django.contrib import messages
from django.contrib.auth.decorators import login_not_required
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.decorators import method_decorator


@method_decorator(login_not_required, name='dispatch')
class SecurityLoginView(LoginView):
    template_name = 'security/login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        messages.success(self.request, f'¡Bienvenido, {form.get_user().get_username()}!')
        return super().form_valid(form)


class SecurityLogoutView(LogoutView):
    """Cierra la sesión (solo por POST) y redirige a LOGOUT_REDIRECT_URL."""
