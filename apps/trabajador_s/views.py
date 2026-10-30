from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from apps.mixins import MinecraftFormMixin
from apps.trabajador_s.models import TrabajadorSocial


class TrabajadorSocialListView(PermissionRequiredMixin, ListView):
    permission_required = 'trabajador_s.view_trabajadorsocial'
    model = TrabajadorSocial
    template_name = 'trabajador_s/list.html'


class TrabajadorSocialCreateView(PermissionRequiredMixin, MinecraftFormMixin, CreateView):
    permission_required = 'trabajador_s.add_trabajadorsocial'
    model = TrabajadorSocial
    fields = ['nombre', 'apellido', 'correo_electronico', 'telefono', 'direccion']
    template_name = 'trabajador_s/create.html'
    success_url = reverse_lazy('trabajador_s:list')
    success_message = 'Trabajador social creado.'
    date_fields = ()
    time_fields = ()


class TrabajadorSocialUpdateView(PermissionRequiredMixin, MinecraftFormMixin, UpdateView):
    permission_required = 'trabajador_s.change_trabajadorsocial'
    model = TrabajadorSocial
    fields = ['nombre', 'apellido', 'correo_electronico', 'telefono', 'direccion']
    template_name = 'trabajador_s/update.html'
    success_url = reverse_lazy('trabajador_s:list')
    success_message = 'Trabajador social actualizado.'
    date_fields = ()
    time_fields = ()


class TrabajadorSocialDeleteView(PermissionRequiredMixin, MinecraftFormMixin, DeleteView):
    permission_required = 'trabajador_s.delete_trabajadorsocial'
    model = TrabajadorSocial
    template_name = 'trabajador_s/delete.html'
    success_url = reverse_lazy('trabajador_s:list')
    success_message = 'Trabajador social eliminado.'


class TrabajadorSocialDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'trabajador_s.view_trabajadorsocial'
    model = TrabajadorSocial
    template_name = 'trabajador_s/detail.html'
