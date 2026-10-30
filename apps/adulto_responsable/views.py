from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from apps.mixins import MinecraftFormMixin
from apps.adulto_responsable.models import AdultoResponsable


class AdultoResponsableListView(PermissionRequiredMixin, ListView):
    permission_required = 'adulto_responsable.view_adultoresponsable'
    model = AdultoResponsable
    template_name = 'adulto_responsable/list.html'


class AdultoResponsableCreateView(PermissionRequiredMixin, MinecraftFormMixin, CreateView):
    permission_required = 'adulto_responsable.add_adultoresponsable'
    model = AdultoResponsable
    fields = ['nombre', 'apellido', 'dni', 'estudiante']
    template_name = 'adulto_responsable/create.html'
    success_url = reverse_lazy('adulto_responsable:list')
    success_message = 'Adulto responsable creado.'
    date_fields = ()
    time_fields = ()


class AdultoResponsableUpdateView(PermissionRequiredMixin, MinecraftFormMixin, UpdateView):
    permission_required = 'adulto_responsable.change_adultoresponsable'
    model = AdultoResponsable
    fields = ['nombre', 'apellido', 'dni', 'estudiante']
    template_name = 'adulto_responsable/update.html'
    success_url = reverse_lazy('adulto_responsable:list')
    success_message = 'Adulto responsable actualizado.'
    date_fields = ()
    time_fields = ()


class AdultoResponsableDeleteView(PermissionRequiredMixin, MinecraftFormMixin, DeleteView):
    permission_required = 'adulto_responsable.delete_adultoresponsable'
    model = AdultoResponsable
    template_name = 'adulto_responsable/delete.html'
    success_url = reverse_lazy('adulto_responsable:list')
    success_message = 'Adulto responsable eliminado.'


class AdultoResponsableDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'adulto_responsable.view_adultoresponsable'
    model = AdultoResponsable
    template_name = 'adulto_responsable/detail.html'
