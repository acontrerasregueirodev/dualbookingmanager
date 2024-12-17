from django.db import models
from django.contrib.auth.models import User

class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20)
    calle = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100, blank=True, null=True)
    pais = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=20)
    notas = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.user.username})"

# Nuevo modelo para archivos asociados a los managers
class ArchivoManager(models.Model):
    manager = models.ForeignKey(Manager, related_name='archivos', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    archivo = models.FileField(upload_to='archivos_managers/')
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.manager}"
