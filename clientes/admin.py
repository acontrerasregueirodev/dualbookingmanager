from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    # Mostrar todos los campos en la lista
    list_display = (
        'id', 'nombre_evento', 'direccion', 'persona_contacto',
        'telefono', 'email', 'notas', 'otros_datos',
        'fecha_creacion', 'ultima_modificacion'
    )
    # Campos editables directamente desde la lista
    list_editable = (
        'nombre_evento', 'direccion', 'persona_contacto',
        'telefono', 'email'
    )
    # Campos para buscar
    search_fields = ('nombre_evento', 'persona_contacto', 'email', 'telefono')
    # Filtros
    list_filter = ('fecha_creacion', 'ultima_modificacion')
    # Orden por defecto
    ordering = ('-fecha_creacion',)
    # Campos de solo lectura
    readonly_fields = ('fecha_creacion', 'ultima_modificacion')
