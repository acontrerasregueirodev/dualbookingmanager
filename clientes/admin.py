from django.contrib import admin
from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    # Definir los campos que se mostrarán en la lista de clientes
    list_display = ('razon_social', 'nombre', 'apellido_1', 'apellido_2', 'email', 'telefono', 'cif', 'numero_cuenta', 'fecha_alta', 'activo')
    
    # Hacer que los campos 'razon_social' y 'cif' sean buscables
    search_fields = ['razon_social', 'nombre', 'apellido_1', 'apellido_2', 'email', 'cif']
    
    # Permitir filtros por estado y fecha de alta
    list_filter = ['activo', 'fecha_alta']
    
    # Definir los campos que se pueden editar en la vista de detalles
    fields = ['razon_social', 'nombre', 'apellido_1', 'apellido_2', 'email', 'telefono', 'cif', 'numero_cuenta', 'direccion', 'ciudad', 'provincia', 'codigo_postal', 'telefono_contacto', 'email_contacto', 'activo']
    
    # Incluir todos los campos en la vista de creación
    add_fieldsets = (
        (None, {
            'fields': ('razon_social', 'nombre', 'apellido_1', 'apellido_2', 'email', 'telefono', 'cif', 'numero_cuenta', 'direccion', 'ciudad', 'provincia', 'codigo_postal', 'telefono_contacto', 'email_contacto', 'activo')
        }),
    )

    # Mostrar un formulario limpio y personalizado si es necesario
    def clean(self, request):
        # Aquí puedes agregar validaciones personalizadas si lo necesitas
        pass

# Registrar el modelo Cliente con la configuración personalizada
admin.site.register(Cliente, ClienteAdmin)
