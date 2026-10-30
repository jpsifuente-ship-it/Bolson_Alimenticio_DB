from django.db import models

class ConfirmacionDeRetiro(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_retiro = models.DateField()
    motivo_retiro = models.TextField()

    def __str__(self):
        return self.nombre

