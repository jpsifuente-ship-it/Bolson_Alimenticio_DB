from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from apps.adulto_responsable.models import AdultoResponsable
from apps.mixins import MinecraftFormMixin
from apps.retiro.forms import RetiroForm
from apps.retiro.models import Retiro


class AdultosPorEstudianteMixin:
    """Pasa al template un mapa {id_estudiante: nombre del adulto} para mostrarlo al elegir."""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mapa = {}
        for adulto in AdultoResponsable.objects.order_by('pk'):
            mapa.setdefault(str(adulto.estudiante_id), str(adulto))
        context['adultos_por_estudiante'] = mapa
        return context


class RetiroListView(PermissionRequiredMixin, ListView):
    permission_required = 'retiro.view_retiro'
    model = Retiro
    template_name = 'retiro/list.html'


class RetiroCreateView(PermissionRequiredMixin, AdultosPorEstudianteMixin, MinecraftFormMixin, CreateView):
    permission_required = 'retiro.add_retiro'
    model = Retiro
    form_class = RetiroForm
    template_name = 'retiro/create.html'
    success_url = reverse_lazy('retiro:list')
    success_message = 'Retiro creado.'


class RetiroUpdateView(PermissionRequiredMixin, AdultosPorEstudianteMixin, MinecraftFormMixin, UpdateView):
    permission_required = 'retiro.change_retiro'
    model = Retiro
    form_class = RetiroForm
    template_name = 'retiro/update.html'
    success_url = reverse_lazy('retiro:list')
    success_message = 'Retiro actualizado.'


class RetiroDeleteView(PermissionRequiredMixin, MinecraftFormMixin, DeleteView):
    permission_required = 'retiro.delete_retiro'
    model = Retiro
    template_name = 'retiro/delete.html'
    success_url = reverse_lazy('retiro:list')
    success_message = 'Retiro eliminado.'


class RetiroDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'retiro.view_retiro'
    model = Retiro
    template_name = 'retiro/detail.html'
