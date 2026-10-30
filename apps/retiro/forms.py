from django import forms

from apps.retiro.models import Retiro


class RetiroForm(forms.ModelForm):
    """El adulto no se elige: se toma del adulto responsable asignado al estudiante."""

    class Meta:
        model = Retiro
        fields = ['estudiante', 'fecha_retiro', 'hora_retiro', 'confirmacion_retiro', 'observacion']
        widgets = {
            'fecha_retiro': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'hora_retiro': forms.TimeInput(attrs={'type': 'time'}, format='%H:%M'),
        }

    def clean_estudiante(self):
        estudiante = self.cleaned_data['estudiante']
        if not estudiante.adultos_responsables.exists():
            raise forms.ValidationError('Este estudiante no tiene un adulto responsable asignado.')
        return estudiante

    def save(self, commit=True):
        retiro = super().save(commit=False)
        retiro.adulto = retiro.estudiante.adultos_responsables.order_by('pk').first()
        if commit:
            retiro.save()
            self.save_m2m()
        return retiro
