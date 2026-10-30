from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from apps.mixins import MinecraftFormMixin
from apps.estudiante.models import Estudiante


class EstudianteListView(PermissionRequiredMixin, ListView):
    permission_required = 'estudiante.view_estudiante'
    model = Estudiante
    template_name = 'estudiante/list.html'


class EstudianteCreateView(PermissionRequiredMixin, MinecraftFormMixin, CreateView):
    permission_required = 'estudiante.add_estudiante'
    model = Estudiante
    fields = ['nombre', 'apellido', 'dni', 'fecha_nacimiento', 'curso', 'colegio']
    template_name = 'estudiante/create.html'
    success_url = reverse_lazy('estudiante:list')
    success_message = 'Estudiante creado.'
    date_fields = ('fecha_nacimiento',)
    time_fields = ()


class EstudianteUpdateView(PermissionRequiredMixin, MinecraftFormMixin, UpdateView):
    permission_required = 'estudiante.change_estudiante'
    model = Estudiante
    fields = ['nombre', 'apellido', 'dni', 'fecha_nacimiento', 'curso', 'colegio']
    template_name = 'estudiante/update.html'
    success_url = reverse_lazy('estudiante:list')
    success_message = 'Estudiante actualizado.'
    date_fields = ('fecha_nacimiento',)
    time_fields = ()


class EstudianteDeleteView(PermissionRequiredMixin, MinecraftFormMixin, DeleteView):
    permission_required = 'estudiante.delete_estudiante'
    model = Estudiante
    template_name = 'estudiante/delete.html'
    success_url = reverse_lazy('estudiante:list')
    success_message = 'Estudiante eliminado.'


class EstudianteDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'estudiante.view_estudiante'
    model = Estudiante
    template_name = 'estudiante/detail.html'
