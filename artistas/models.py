from django.db import models

class Artista(models.Model):
    nombre_artistico = models.CharField(max_length=255)  # Nombre artístico
    nombre = models.CharField(max_length=255)
    apellido_1 = models.CharField(max_length=255)
    apellido_2 = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    activo = models.BooleanField(default=True)  # Si el artista está activo
    disponibilidad = models.BooleanField(default=True)  # Si el artista está disponible para eventos
    fecha_registro = models.DateTimeField(auto_now_add=True)  # Fecha en que se registró el artista

    def __str__(self):
        return f"{self.nombre_artistico if self.nombre_artistico else self.nombre} {self.apellido_1}"

    class Meta:
        db_table = 'artistas_artista'  # Define el nombre de la tabla
        ordering = ['nombre_artistico']  # Orden predeterminado por nombre
        

class Foto(models.Model):
    artista = models.ForeignKey(Artista, related_name='fotos', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    # Cambia el subdirectorio a 'media/fotos/'
    foto_url = models.ImageField(upload_to='fotos/')  
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Foto de {self.artista.nombre} ({self.descripcion})"




class Documento(models.Model):
    artista = models.ForeignKey(Artista, related_name='documentos', on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='artista/documentos/')  # Ruta donde se suben los documentos
    descripcion = models.CharField(max_length=255, blank=True, null=True)  # Descripción del documento
    titulo = models.CharField(max_length=255)  # Título del documento
    fecha_subida = models.DateTimeField(auto_now_add=True)  # Fecha en que se subió el documento

    def __str__(self):
        return f"Documento de {self.artista.nombre} - {self.titulo}"
