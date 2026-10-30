from django.db import models

class Retiro(models.Model):
    estudiante = models.ForeignKey('estudiante.Estudiante', on_delete=models.CASCADE)
    adulto = models.ForeignKey('adulto_responsable.AdultoResponsable', on_delete=models.CASCADE)
    fecha_retiro = models.DateField()
    hora_retiro = models.TimeField()
    confirmacion_retiro = models.BooleanField(default=False)
    observacion = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"{self.estudiante} - {self.fecha_retiro}"
