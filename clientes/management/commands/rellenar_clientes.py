import random
from django.core.management.base import BaseCommand
from faker import Faker
from clientes.models import Cliente

class Command(BaseCommand):
    help = "Rellena la base de datos con datos ficticios para el modelo Cliente"

    def handle(self, *args, **kwargs):
        # Inicializar Faker
        fake = Faker('es_ES')  # Genera datos en español

        # Número de clientes a crear
        num_clientes = 50

        # Borrar datos existentes (opcional)
        Cliente.objects.all().delete()

        for _ in range(num_clientes):
            cliente = Cliente.objects.create(
                nombre_evento=fake.company(),
                direccion=fake.address(),
                persona_contacto=fake.name(),
                telefono=fake.phone_number(),
                email=fake.email(),
                notas=fake.text(max_nb_chars=200),
                otros_datos={"extra_info": fake.word()},
            )
            self.stdout.write(self.style.SUCCESS(f"Cliente creado: {cliente.nombre_evento}"))

        self.stdout.write(self.style.SUCCESS(f"Se han generado {num_clientes} clientes."))
