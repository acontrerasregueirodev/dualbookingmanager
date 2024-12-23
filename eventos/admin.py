from django.contrib import admin
from .models import Evento

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'cliente', 'nombre', 'fecha', 'fecha_fin', 
        'hora_inicio', 'hora_fin', 'direccion', 'descripcion', 'estado', 'get_artistas'
    )
    list_filter = ('fecha', 'fecha_fin', 'estado')
    search_fields = ('nombre', 'direccion', 'cliente__nombre_evento')
    ordering = ('-fecha',)
    readonly_fields = ('id',)
    
    # Personaliza la disposición de los campos en el formulario
    fieldsets = (
        (None, {
            'fields': (
                'cliente', 
                ('nombre'),
                'direccion',
                ('fecha', 'fecha_fin'),  # Fecha y Fecha Fin en la misma línea
                ('hora_inicio', 'hora_fin'),  # Hora Inicio y Hora Fin en la misma línea
                'artistas',  # 'artistas' después de 'descripcion'
                ('estado', 'descripcion'),  # Estado y Descripción en la misma línea
            ),
            'classes': ('wide', 'form-row'),  # Se añade 'form-row' para alineación
        }),
    )

    # Método para mostrar los nombres de los artistas asociados al evento
    def get_artistas(self, obj):
        return ", ".join([artista.nombre for artista in obj.artistas.all()])
    get_artistas.short_description = 'Artistas'

    # Agregar filtro horizontal para el campo de ManyToMany
    filter_horizontal = ('artistas',)
