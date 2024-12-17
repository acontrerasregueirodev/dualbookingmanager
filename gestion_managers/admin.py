# admin.py en gestion_managers

from django.contrib import admin
from django.contrib.auth.models import User
from .models import Manager, ArchivoManager
from .forms import ManagerForm  # Importamos el formulario personalizado

class ArchivoManagerInline(admin.TabularInline):
    model = ArchivoManager
    extra = 1  # Muestra un formulario vacío adicional
class ManagerAdmin(admin.ModelAdmin):
    form = ManagerForm  # Usamos el formulario personalizado

    list_display = ('user', 'telefono', 'calle', 'ciudad', 'estado', 'pais', 'codigo_postal', 'email')
    search_fields = ('user__username', 'telefono', 'email')
    list_filter = ('estado', 'pais')
    ordering = ('user',)

    def save_model(self, request, obj, form, change):
        # Verificar si el objeto ya tiene un usuario asignado sin provocar un error
        if not obj.pk or not hasattr(obj, 'user'):
            # Crear un nuevo usuario automáticamente
            user = User.objects.create_user(
                username=obj.telefono,  # Usamos el teléfono como username
                password="defaultpassword",  # Contraseña por defecto
                email=obj.email,
                first_name=getattr(obj, 'nombre', ''),  # Evita errores si 'nombre' no existe
                last_name=getattr(obj, 'apellidos', '')  # Evita errores si 'apellidos' no existe
            )
            obj.user = user  # Asociar el usuario al manager

        # Guardar el objeto Manager
        super().save_model(request, obj, form, change)
    

# Registrar el modelo Manager en el admin
admin.site.register(Manager, ManagerAdmin)
admin.site.register(ArchivoManager)

