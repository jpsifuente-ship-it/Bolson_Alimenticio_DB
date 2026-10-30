from django import forms
from django.contrib.messages.views import SuccessMessageMixin


class MinecraftFormMixin(SuccessMessageMixin):
    """Muestra mensajes de éxito y usa selectores nativos de fecha y hora."""
    date_fields = ()
    time_fields = ()

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for nombre in self.date_fields:
            if nombre in form.fields:
                form.fields[nombre].widget = forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d')
        for nombre in self.time_fields:
            if nombre in form.fields:
                form.fields[nombre].widget = forms.TimeInput(attrs={'type': 'time'}, format='%H:%M')
        return form
