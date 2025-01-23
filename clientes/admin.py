from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    # Mostrar los campos de manera ordenada y ajustada
    list_display = (
        'id', 'nombre_evento', 'direccion', 'persona_contacto',
        'telefono', 'email', 'notas', 'otros_datos',
        'fecha_creacion', 'ultima_modificacion'
    )

    # Agregar búsqueda por campos clave
    search_fields = ('nombre_evento', 'persona_contacto', 'email', 'telefono')

    # Agregar filtros para mejorar la navegación
    list_filter = ('fecha_creacion', 'ultima_modificacion')

    # Ordenar la lista por fecha de creación de manera descendente
    ordering = ('-fecha_creacion',)

    # Definir campos de solo lectura
    readonly_fields = ('fecha_creacion', 'ultima_modificacion')

    # Personalizar la forma en que se ven los formularios en la vista de edición
    fieldsets = (
        (None, {
            'fields': ('nombre_evento', 'direccion', 'persona_contacto', 'telefono', 'email', 'notas')
        }),
        ('Datos adicionales', {
            'fields': ('otros_datos',),
        }),
        ('Fechas', {
            'fields': ('fecha_creacion', 'ultima_modificacion'),
            'classes': ('collapse',),  # Ocultar por defecto los campos de fechas
        }),
    )

    # Hacer que los enlaces de las filas sean en el campo 'id' para facilitar la navegación
    list_display_links = ('id', 'nombre_evento')

    # Mejorar el espaciado y la legibilidad
    list_per_page = 15  # Limitar la cantidad de registros por página

    # Otras configuraciones opcionales
    actions_on_top = True  # Mostrar las acciones en la parte superior
    actions_on_bottom = True  # Mostrar las acciones en la parte inferior


