from django.contrib import admin
from .models import DJ, Manager, Evento, Foto, Documento

# Administrar el modelo Manager
@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido_1', 'apellido_2', 'email', 'telefono']
    search_fields = ['nombre', 'apellido_1', 'apellido_2', 'email']
    list_filter = ['apellido_1', 'apellido_2']
    ordering = ['apellido_1', 'apellido_2', 'nombre']

# Administrar el modelo DJ
@admin.register(DJ)
class DJAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido_1', 'apellido_2', 'nombre_artistico', 'direccion', 'telefono', 'email', 'tarifa_hora', 'experiencia', 'activo', 'disponibilidad', 'manager']
    search_fields = ['nombre', 'apellido_1', 'apellido_2', 'nombre_artistico', 'email', 'direccion', 'manager__nombre']
    list_filter = ['activo', 'disponibilidad', 'manager']
    ordering = ['apellido_1', 'apellido_2', 'nombre']
    # Eliminar filter_horizontal ya que no es necesario para una relación ForeignKey

# Administrar el modelo Evento
@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'fecha_evento', 'lugar', 'descripcion']
    search_fields = ['nombre', 'lugar', 'descripcion']
    list_filter = ['fecha_evento']
    ordering = ['fecha_evento']

# Administrar el modelo Foto
@admin.register(Foto)
class FotoAdmin(admin.ModelAdmin):
    list_display = ['dj', 'descripcion', 'foto_url']
    search_fields = ['dj__nombre', 'descripcion', 'foto_url']
    list_filter = ['dj']
    ordering = ['dj', 'descripcion']

# Administrar el modelo Documento
@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ['dj', 'archivo', 'descripcion']
    search_fields = ['dj__nombre', 'archivo', 'descripcion']
    list_filter = ['dj']
    ordering = ['dj', 'descripcion']
