import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from eventos.models import Evento
from clientes.models import Cliente
from artistas.models import Artista
from datetime import timedelta

class Command(BaseCommand):
    help = 'Genera 50 eventos asignados a clientes y DJs de manera aleatoria.'

    def handle(self, *args, **kwargs):
        # Obtener todos los clientes y DJs existentes
        clientes = Cliente.objects.all()
        artistas = Artista.objects.all()

        if not clientes or not artistas:
            self.stdout.write(self.style.ERROR('No hay clientes o DJs en la base de datos.'))
            return
        
        for i in range(50):
            # Seleccionar un cliente y un DJ aleatorios
            cliente = random.choice(clientes)
            artista = random.choice(artistas)
            
            # Generar una fecha de evento aleatoria dentro del próximo mes
            fecha = timezone.now() + timedelta(days=random.randint(1, 30))
            fecha_fin = fecha + timedelta(days=random.randint(1, 3))  # Evento de 1 a 3 días

            # Generar horas aleatorias para el inicio y fin
            hora_inicio = timezone.datetime(2024, 1, 1, random.randint(10, 18), random.randint(0, 59))
            hora_fin = hora_inicio + timedelta(hours=random.randint(1, 3))  # Duración del evento entre 1 y 3 horas
            
            # Crear evento aleatorio
            evento = Evento.objects.create(
                cliente=cliente,
                nombre=f"Evento {i + 1}",
                fecha=fecha.date(),
                fecha_fin=fecha_fin.date(),
                hora_inicio=hora_inicio.time(),
                hora_fin=hora_fin.time(),
                direccion=f"Dirección {random.randint(1, 100)}",
                descripcion=f"Descripción del evento {i + 1}",
                estado=random.choice(['pendiente', 'confirmado', 'cancelado'])
            )
            # Asignar el DJ al evento (si la relación es Many-to-Many)
            evento.artistas.add(artista)  # Si usas ForeignKey: evento.artista = dj

            self.stdout.write(self.style.SUCCESS(f'Evento "{evento.nombre}" creado con DJ "{artista.nombre}" exitosamente.'))
