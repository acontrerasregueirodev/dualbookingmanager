from django.db import models

class Cliente(models.Model):
    # Información básica del cliente
    nombre = models.CharField(max_length=255)
    apellido_1 = models.CharField(max_length=255)
    apellido_2 = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True, null=True)
    
    # Nombre o razón social
    razon_social = models.CharField(max_length=255, blank=True, null=True)  # Razón social para empresas

    # Datos fiscales y financieros
    cif = models.CharField(max_length=9, unique=True)  # CIF (para empresas)
    numero_cuenta = models.CharField(max_length=24, blank=True, null=True)  # IBAN o número de cuenta
    direccion = models.CharField(max_length=255, blank=True, null=True)
    ciudad = models.CharField(max_length=255, blank=True, null=True)
    provincia = models.CharField(max_length=255, blank=True, null=True)
    codigo_postal = models.CharField(max_length=10, blank=True, null=True)
    
    # Datos adicionales
    fecha_alta = models.DateField(auto_now_add=True)  # Fecha en que se dio de alta el cliente
    activo = models.BooleanField(default=True)  # Si el cliente está activo

    # Datos de contacto adicional
    telefono_contacto = models.CharField(max_length=20, blank=True, null=True)
    email_contacto = models.EmailField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.razon_social if self.razon_social else self.nombre} {self.apellido_1} ({self.cif})"
