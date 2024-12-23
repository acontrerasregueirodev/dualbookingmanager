from django.db import models

class Cliente(models.Model):
    # Información principal del cliente
    nombre_evento = models.CharField(
        max_length=255,
        verbose_name="Nombre de la discoteca o festival",
        help_text="Nombre del lugar o evento"
    )
    direccion = models.TextField(
        verbose_name="Dirección de la sala",
        help_text="Dirección completa del lugar del evento"
    )

    # Datos de contacto asociados
    persona_contacto = models.CharField(
        max_length=255,
        verbose_name="Persona de contacto",
        help_text="Nombre completo de la persona de contacto"
    )
    telefono = models.CharField(
        max_length=15,
        verbose_name="Teléfono de contacto",
        null=True,
        blank=True
    )
    email = models.EmailField(
        verbose_name="Correo electrónico de contacto",
        null=True,
        blank=True
    )

    # Datos adicionales
    notas = models.TextField(
        verbose_name="Notas adicionales",
        blank=True,
        help_text="Cualquier información adicional relevante sobre el cliente"
    )
    otros_datos = models.JSONField(
        verbose_name="Otros datos",
        blank=True,
        null=True,
        help_text="Campo flexible para almacenar información adicional"
    )

    # Campos de auditoría
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    ultima_modificacion = models.DateTimeField(auto_now=True, verbose_name="Última modificación")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["-fecha_creacion"]

    def __str__(self):
        return f"{self.nombre_evento} - {self.persona_contacto}"
