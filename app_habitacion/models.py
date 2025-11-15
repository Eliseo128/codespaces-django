from django.db import models

# Create your models here.
class Habitacion(models.Model):
    TIPO_HABITACION = [
        ('individual', 'Individual'),
        ('doble', 'Doble'),
        ('suite', 'Suite'),
        ('uci', 'UCI'),
    ]
    
    ESTADO_HABITACION = [
        ('disponible', 'Disponible'),
        ('ocupada', 'Ocupada'),
        ('mantenimiento', 'En Mantenimiento'),
        ('limpieza', 'En Limpieza'),
    ]
    
    id_habitacion = models.AutoField(primary_key=True)
    numero_habitacion = models.CharField(max_length=10, unique=True)
    tipo_habitacion = models.CharField(max_length=50, choices=TIPO_HABITACION)
    estado_habitacion = models.CharField(max_length=50, choices=ESTADO_HABITACION)
    costo_diario = models.DecimalField(max_digits=10, decimal_places=2)
    capacidad = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Habitación {self.numero_habitacion} - {self.tipo_habitacion}"