from django.db import models
from apps.estudiante.models import Estudiante

class AdultoResponsable(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='adultos_responsables')
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"