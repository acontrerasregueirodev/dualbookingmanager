from django.db import models
from django.conf import settings
from  artistas.models import Manager,DJ
from clientes.models import Cliente
from gestion_managers.models import Manager
class Evento(models.Model):
    # Referencia al modelo Cliente
    cliente = models.ForeignKey('clientes.Cliente', related_name='eventos', on_delete=models.CASCADE)
    
    # Referencia al modelo DJ
    dj = models.ForeignKey('artistas.DJ', related_name='eventos', on_delete=models.CASCADE)
    
    # Referencia al modelo Manager
    manager = models.ForeignKey('gestion_managers.Manager', related_name='eventos', on_delete=models.CASCADE)
    
    # Otros campos del evento
    nombre_evento = models.CharField(max_length=255)
    fecha_evento = models.DateTimeField()  # Incluye la fecha y la hora del evento
    descripcion = models.TextField(blank=True, null=True)
    lugar = models.CharField(max_length=255)
    
    # Información sobre el transporte
    transporte = models.CharField(max_length=255, blank=True, null=True)  # Ej: "Taxi", "Autobús", etc.
    hora_llegada_avion = models.DateTimeField(blank=True, null=True)  # Hora de llegada del avión
    quien_recoge = models.CharField(max_length=255, blank=True, null=True)  # Quién te recoge (nombre o empresa)
    telefono_contacto_exterior = models.CharField(max_length=20, blank=True, null=True)  # Teléfono de contacto en el exterior

    # Google Calendar ID
    google_event_id = models.CharField(max_length=255, blank=True, null=True)

    # Fecha de creación del evento en la base de datos
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Evento: {self.nombre_evento} ({self.fecha_evento})"

    def save(self, *args, **kwargs):
        # Puedes agregar lógica para actualizar Google Calendar cuando se guarde el evento
        super().save(*args, **kwargs)
