import os
from django.utils.html import format_html
from django.urls import reverse
from django.contrib import admin
from django import forms
from django.utils.html import mark_safe
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Artista, Foto, Documento

# Formulario personalizado para mostrar la vista previa de la imagen
class ImagePreviewWidget(forms.ClearableFileInput):
    def render(self, name, value, attrs=None, renderer=None):
        output = super().render(name, value, attrs, renderer)
        if value and hasattr(value, "url"):
            output = f'<img src="{value.url}" width="100" height="100" style="display:block; margin-bottom: 10px;" />' + output
        return mark_safe(output)

class FotoForm(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ['foto_url', 'descripcion']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.foto_url:
            self.fields['foto_url'].widget.attrs['readonly'] = True
            self.fields['foto_url'].help_text = format_html(
                '<img src="{}" width="100" height="100" style="margin: 5px 0;" />',
                self.instance.foto_url.url,
            )

class FotoInline(admin.TabularInline):
    model = Foto
    form = FotoForm
    extra = 0
    fields = ['foto_url', 'descripcion', 'acciones']
    readonly_fields = ['acciones']
    show_change_link = True

    def acciones(self, obj):
        if obj.foto_url:
            foto_url = obj.foto_url.url
            editar_url = reverse('admin:artistas_foto_change', args=[obj.id])
            eliminar_url = reverse('admin:artistas_foto_delete', args=[obj.id])

            return format_html(
                '<a href="{}" target="_blank">Ver foto</a> | '
                '<a href="{}" class="button" style="color: green;">Guardar</a> | '
                '<a href="{}" class="button delete-link" style="color: red;">Eliminar</a>',
                foto_url,
                editar_url,
                eliminar_url
            )
        return ""

    acciones.short_description = 'Acciones'

    def has_delete_permission(self, request, obj=None):
        return False

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ['titulo', 'descripcion', 'archivo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.archivo:
            self.fields['archivo'].widget.attrs['readonly'] = True
            self.fields['archivo'].help_text = format_html(
                '<a href="{}" target="_blank">Ver documento</a>',
                self.instance.archivo.url,
            )
        else:
            self.fields['archivo'].help_text = "Selecciona un archivo para cargar"

class DocumentoInline(admin.TabularInline):
    model = Documento
    form = DocumentoForm
    extra = 0
    fields = ['titulo', 'descripcion', 'acciones', 'archivo']
    readonly_fields = ['acciones']
    show_change_link = True

    def acciones(self, obj):
        if obj.archivo:
            archivo_url = obj.archivo.url
            editar_url = reverse('admin:artistas_documento_change', args=[obj.id])
            eliminar_url = reverse('admin:artistas_documento_delete', args=[obj.id])

            return format_html(
                '<a href="{}" class="button" style="color: green;">Guardar</a> | '
                '<a href="{}" class="button delete-link" style="color: red;">Eliminar</a>',
                editar_url,
                eliminar_url
            )
        return ""

    acciones.short_description = 'Acciones'

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nombre_artistico', 'activo', 'disponibilidad')
    list_display_links = ('nombre', 'nombre_artistico')
    search_fields = ('nombre', 'nombre_artistico')
    ordering = ['nombre']
    list_per_page = 20
    inlines = [FotoInline, DocumentoInline]

# Eliminar archivos físicos al eliminar objetos
@receiver(post_delete, sender=Foto)
def eliminar_archivo_foto(sender, instance, **kwargs):
    if instance.foto_url and os.path.isfile(instance.foto_url.path):
        os.remove(instance.foto_url.path)

@receiver(post_delete, sender=Documento)
def eliminar_archivo_documento(sender, instance, **kwargs):
    if instance.archivo and os.path.isfile(instance.archivo.path):
        os.remove(instance.archivo.path)

# Registro de modelos
admin.site.register(Foto)
admin.site.register(Documento)