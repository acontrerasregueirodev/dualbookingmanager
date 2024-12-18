from django.core.management.base import BaseCommand
from artistas.models import Artista, Foto, Documento
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Rellena la base de datos con datos ficticios para Artistas, Fotos y Documentos'

    def handle(self, *args, **kwargs):
        fake = Faker('es_ES')  # Usar datos en español para más realismo

        # Crear Artistas
        self.stdout.write('Creando artistas...')
        artistas = []
        for _ in range(30):  # Cambia el número para más o menos artistas
            artista = Artista.objects.create(
                nombre_artistico=fake.first_name() + " " + fake.last_name(),
                nombre=fake.first_name(),
                apellido_1=fake.last_name(),
                apellido_2=fake.last_name(),
                direccion=fake.address(),
                telefono=fake.phone_number(),
                email=fake.email(),
                activo=random.choice([True, False]),
                disponibilidad=random.choice([True, False]),
            )
            artistas.append(artista)

        # Crear Fotos para cada artista
        self.stdout.write('Creando fotos...')
        for artista in artistas:
            for _ in range(random.randint(1, 3)):  # Entre 1 y 3 fotos por artista
                Foto.objects.create(
                    artista=artista,
                    descripcion=fake.sentence(),
                    foto_url=fake.image_url(),
                )

        # Crear Documentos para cada artista
        self.stdout.write('Creando documentos...')
        for artista in artistas:
            for _ in range(random.randint(1, 2)):  # Entre 1 y 2 documentos por artista
                Documento.objects.create(
                    artista=artista,
                    titulo=fake.sentence(nb_words=4),
                    descripcion=fake.sentence(),
                    archivo=f'artista/documentos/{fake.word()}.{random.choice(["pdf"])}',
                )

        self.stdout.write(self.style.SUCCESS('Datos ficticios creados con éxito.'))
