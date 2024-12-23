# admin.py
from django.contrib import admin
from .models import Artista, Foto, Documento
from django import forms
from django.utils.html import mark_safe

# Define el widget personalizado para mostrar una vista previa de la imagen
class ImagePreviewWidget(forms.ClearableFileInput):
    def render(self, name, value, attrs=None, renderer=None):
        # Si ya hay una URL de imagen, muestra una miniatura
        if value:
            return mark_safe(f'<img src="{value}" width="100" height="100" />')
        return super().render(name, value, attrs, renderer)

# Crear un formulario para el modelo Foto
class FotoForm(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ['descripcion', 'foto_url']  # Los campos que quieres mostrar

    # Usar el widget personalizado para 'foto_url'
    foto_url = forms.ImageField(widget=ImagePreviewWidget, required=False)

# Inline para las fotos relacionadas con un Artista
class FotoInline(admin.TabularInline):
    model = Foto
    extra = 1  # Número de formularios vacíos que se muestran por defecto
    form = FotoForm  # Usar el formulario personalizado con el widget
    fields = ['foto_url', 'descripcion']  # Primero la imagen, luego la descripción
    readonly_fields = ['fecha_subida']  # Asegura que 'fecha_subida' solo sea visible, no editable

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

