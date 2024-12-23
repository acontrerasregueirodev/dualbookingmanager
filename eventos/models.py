from django.db import models
from artistas.models import Artista  
from clientes.models import Cliente

class Evento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="eventos")
    nombre = models.CharField(max_length=255)
    fecha = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    direccion = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    estado = models.CharField(
        max_length=20,
        choices=[
            ('pendiente', 'Pendiente'),
            ('confirmado', 'Confirmado'),
            ('cancelado', 'Cancelado'),
        ],
        default='pendiente'
    )
    # Relación Many-to-Many con DJs
    artistas = models.ManyToManyField(Artista, related_name='eventos', blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.cliente.nombre_evento})"
