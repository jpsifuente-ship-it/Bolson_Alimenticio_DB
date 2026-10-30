from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from apps.mixins import MinecraftFormMixin
from apps.punto_de_entrega.models import ConfirmacionDeRetiro


class PuntoDeEntregaListView(PermissionRequiredMixin, ListView):
    permission_required = 'punto_de_entrega.view_confirmacionderetiro'
    model = ConfirmacionDeRetiro
    template_name = 'punto_de_entrega/list.html'


class PuntoDeEntregaCreateView(PermissionRequiredMixin, MinecraftFormMixin, CreateView):
    permission_required = 'punto_de_entrega.add_confirmacionderetiro'
    model = ConfirmacionDeRetiro
    fields = ['nombre', 'fecha_retiro', 'motivo_retiro']
    template_name = 'punto_de_entrega/create.html'
    success_url = reverse_lazy('punto_de_entrega:list')
    success_message = 'Punto de entrega creado.'
    date_fields = ('fecha_retiro',)
    time_fields = ()


class PuntoDeEntregaUpdateView(PermissionRequiredMixin, MinecraftFormMixin, UpdateView):
    permission_required = 'punto_de_entrega.change_confirmacionderetiro'
    model = ConfirmacionDeRetiro
    fields = ['nombre', 'fecha_retiro', 'motivo_retiro']
    template_name = 'punto_de_entrega/update.html'
    success_url = reverse_lazy('punto_de_entrega:list')
    success_message = 'Punto de entrega actualizado.'
    date_fields = ('fecha_retiro',)
    time_fields = ()


class PuntoDeEntregaDeleteView(PermissionRequiredMixin, MinecraftFormMixin, DeleteView):
    permission_required = 'punto_de_entrega.delete_confirmacionderetiro'
    model = ConfirmacionDeRetiro
    template_name = 'punto_de_entrega/delete.html'
    success_url = reverse_lazy('punto_de_entrega:list')
    success_message = 'Punto de entrega eliminado.'


class PuntoDeEntregaDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'punto_de_entrega.view_confirmacionderetiro'
    model = ConfirmacionDeRetiro
    template_name = 'punto_de_entrega/detail.html'
