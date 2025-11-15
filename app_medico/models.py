from django.db import models

# Create your models here.
class Medico(models.Model):
    id_medico = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    licencia_medica = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_contratacion = models.DateField()
    
    def __str__(self):
        return f"Dr. {self.nombre} {self.apellido} - {self.especialidad}"