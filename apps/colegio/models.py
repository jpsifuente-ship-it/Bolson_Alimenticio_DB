from django.db import models

class Colegio(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    correo_electronico = models.EmailField()
    numero_telefono = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre