from django.db import models

class Manager(models.Model):
    nombre = models.CharField(max_length=255)
    apellido_1 = models.CharField(max_length=255)
    apellido_2 = models.CharField(max_length=255)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido_1}"

class Evento(models.Model):
    nombre = models.CharField(max_length=255)
    fecha_evento = models.DateField()
    lugar = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class DJ(models.Model):
    nombre = models.CharField(max_length=255)
    apellido_1 = models.CharField(max_length=255)
    apellido_2 = models.CharField(max_length=255)
    nombre_artistico = models.CharField(max_length=255, blank=True, null=True)  # Nuevo campo para el nombre artístico
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()
    tarifa_hora = models.DecimalField(max_digits=8, decimal_places=2)
    experiencia = models.IntegerField()  # años de experiencia
    activo = models.BooleanField(default=True)  # Si el DJ está activo
    manager = models.ForeignKey(Manager, related_name='djs', on_delete=models.CASCADE)
    disponibilidad = models.BooleanField(default=True)  # Si el DJ está disponible para eventos

    def __str__(self):
        return f"{self.nombre_artistico if self.nombre_artistico else self.nombre} {self.apellido_1}"
class Foto(models.Model):
    dj = models.ForeignKey(DJ, related_name='fotos', on_delete=models.CASCADE)  # Relación con DJ
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    foto_url = models.URLField()  # URL de la foto, en lugar de un campo FileField

    def __str__(self):
        return f"Foto de {self.dj.nombre} ({self.descripcion})"

class Documento(models.Model):
    dj = models.ForeignKey(DJ, related_name='documentos', on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='djs/documentos/')  # Archivo del documento
    descripcion = models.CharField(max_length=255, blank=True, null=True)  # Descripción del documento

    def __str__(self):
        return f"Documento de {self.dj.nombre}"
