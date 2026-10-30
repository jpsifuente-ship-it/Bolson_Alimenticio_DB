from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from apps.mixins import MinecraftFormMixin
from apps.colegio.models import Colegio


class ColegioListView(PermissionRequiredMixin, ListView):
    permission_required = 'colegio.view_colegio'
    model = Colegio
    template_name = 'colegio/list.html'


class ColegioCreateView(PermissionRequiredMixin, MinecraftFormMixin, CreateView):
    permission_required = 'colegio.add_colegio'
    model = Colegio
    fields = '__all__'
    template_name = 'colegio/create.html'
    success_url = reverse_lazy('colegio:list')
    success_message = 'Colegio creado.'
    date_fields = ()
    time_fields = ()


class ColegioUpdateView(PermissionRequiredMixin, MinecraftFormMixin, UpdateView):
    permission_required = 'colegio.change_colegio'
    model = Colegio
    fields = '__all__'
    template_name = 'colegio/update.html'
    success_url = reverse_lazy('colegio:list')
    success_message = 'Colegio actualizado.'
    date_fields = ()
    time_fields = ()


class ColegioDeleteView(PermissionRequiredMixin, MinecraftFormMixin, DeleteView):
    permission_required = 'colegio.delete_colegio'
    model = Colegio
    template_name = 'colegio/delete.html'
    success_url = reverse_lazy('colegio:list')
    success_message = 'Colegio eliminado.'


class ColegioDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'colegio.view_colegio'
    model = Colegio
    template_name = 'colegio/detail.html'
