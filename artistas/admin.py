# admin.py
from django.utils.html import format_html
from django.urls import reverse
from django.contrib import admin
from .models import Artista, Foto, Documento
from django import forms
from django.utils.html import mark_safe

class ImagePreviewWidget(forms.ClearableFileInput):
    def render(self, name, value, attrs=None, renderer=None):
        output = super().render(name, value, attrs, renderer)
        # Si value es un archivo subido o ya existe en el modelo
        if value and hasattr(value, "url"):
            output = f'<img src="{value.url}" width="100" height="100" style="display:block; margin-bottom: 10px;" />' + output
        return mark_safe(output)

class FotoForm(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ['foto_url', 'descripcion']

    # Permitir la vista previa de la imagen
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.foto_url:
            # Mostrar una miniatura de la imagen si ya está subida
            self.fields['foto_url'].widget.attrs['readonly'] = True
            self.fields['foto_url'].help_text = format_html(
                '<img src="{}" width="100" height="100" style="margin: 5px 0;" />',
                self.instance.foto_url.url,  # Aquí accedemos a la URL de la imagen
            )

# Inline personalizado

class FotoInline(admin.TabularInline):
    model = Foto
    form = FotoForm
    extra = 0  # Evitar formularios vacíos por defecto
    fields = ['foto_url', 'descripcion', 'acciones']  # Asegúrate de que 'acciones' sea el único campo visible
    readonly_fields = ['acciones']  # Asegura que la columna 'acciones' solo sea de lectura
    show_change_link = True  # Esto permite que el enlace de "Ver foto" funcione

    # Botones personalizados
    def acciones(self, obj):
        if obj.foto_url:
            foto_url = obj.foto_url.url  # URL completa de la imagen
            editar_url = reverse('admin:artistas_foto_change', args=[obj.id])  # Enlace para editar la foto
            eliminar_url = reverse('admin:artistas_foto_delete', args=[obj.id])  # Enlace para eliminar la foto

            return format_html(
                '<a href="{}" target="_blank">Ver foto</a> | '
                '<a href="{}" class="button" style="color: green;">Guardar</a> | '  # Botón de guardar (editar)
                '<a href="{}" class="button delete-link" style="color: red;">Eliminar</a>',  # Botón de eliminar
                foto_url,  # Enlace a la imagen
                editar_url,  # Enlace para editar la foto (guardar)
                eliminar_url  # Enlace para eliminar la foto
            )
        return ""  # Si no hay foto, no devuelve nada para las acciones
    
    acciones.short_description = 'Acciones'  # Descripción de la columna

    def has_delete_permission(self, request, obj=None):
        return False  # Deshabilitar la opción de eliminación en el inline



# Inline para los documentos relacionados con un Artista
class DocumentoInline(admin.TabularInline):
    model = Documento
    extra = 1  # Número de formularios vacíos que se muestran por defecto
    fields = ['titulo', 'descripcion', 'archivo']  # Elimina 'fecha_subida', ya que no es editable
    readonly_fields = ['fecha_subida']  # Asegura que 'fecha_subida' solo sea visible, no editable

@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nombre_artistico', 'activo', 'disponibilidad')  # Campos visibles en el listado
    list_display_links = ('nombre', 'nombre_artistico')  # Campos clicables
    search_fields = ('nombre', 'nombre_artistico')  # Barra de búsqueda
    ordering = ['nombre']  # Orden predeterminado en el listado
    list_display = [field.name for field in Artista._meta.fields if field.name != 'fecha_registro']  # Excluir 'fecha_registro' del listado
    list_per_page = 20  # Número de registros por página
    inlines = [FotoInline, DocumentoInline]  # Añadir las fotos y documentos como inlines

admin.site.register(Foto)  # Registro de las fotos en el admin
admin.site.register(Documento)  # Registro de los documentos en el admin

