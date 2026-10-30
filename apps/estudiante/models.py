from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.IntegerField()
    fecha_nacimiento = models.DateField()
    curso = models.CharField(max_length=200)
    colegio = models.ForeignKey('colegio.Colegio', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"