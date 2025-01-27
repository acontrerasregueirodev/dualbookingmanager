from django.contrib import admin
from django.urls import path
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404, render, redirect
from django.utils.html import format_html
from django.contrib import messages
from .models import Evento
from django.contrib.staticfiles.storage import staticfiles_storage


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    class Media:
        js = [staticfiles_storage.url('eventos/js/modal.js')]
        css = {
            'all': [staticfiles_storage.url('eventos/css/modal.css')]
        }
    list_display = (
        'id', 'cliente', 'nombre', 'fecha', 'fecha_fin', 
        'hora_inicio', 'hora_fin', 'direccion', 'descripcion', 'estado', 'get_artistas', 'enviar_email'
    )
    list_filter = ('fecha', 'fecha_fin', 'estado')
    search_fields = ('nombre', 'direccion', 'cliente__nombre_evento')
    ordering = ('-fecha',)
    readonly_fields = ('id',)
    filter_horizontal = ('artistas',)

    # Personaliza la disposición de los campos en el formulario
    fieldsets = (
        (None, {
            'fields': (
                'cliente', 
                'nombre',
                'direccion',
                ('fecha', 'fecha_fin'),  # Fecha y Fecha Fin en la misma línea
                ('hora_inicio', 'hora_fin'),  # Hora Inicio y Hora Fin en la misma línea
                'artistas',
                ('estado', 'descripcion'),  # Estado y Descripción en la misma línea
            ),
            'classes': ('wide', 'form-row'),
        }),
    )

    # Método para mostrar los nombres de los artistas asociados al evento
    def get_artistas(self, obj):
        return ", ".join([artista.nombre for artista in obj.artistas.all()])
    get_artistas.short_description = 'Artistas'

    # Método para mostrar el botón de enviar email
    def enviar_email(self, obj):
        return format_html(
            '<a class="button" href="{}" onclick="return showModal(event, \'{}\');">Enviar Email</a>',
            f"{obj.id}/modal-enviar-email/",
            obj.id,
        )
    enviar_email.short_description = 'Acción'
    enviar_email.allow_tags = True

    # Sobrescribir URLs del administrador para añadir una acción personalizada
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                '<int:evento_id>/modal-enviar-email/',
                self.admin_site.admin_view(self.modal_enviar_email),
                name='modal_enviar_email',
            ),
        ]
        return custom_urls + urls

    # Vista para manejar el popup/modal y enviar emails
    def modal_enviar_email(self, request, evento_id):
        if request.method == "POST":
            # Manejo de archivos y envío del correo
            try:
                evento = get_object_or_404(Evento, id=evento_id)
                archivos = request.FILES.getlist('archivos')
                artistas = evento.artistas.all()
                emails = [artista.email for artista in artistas if artista.email]

                if not emails:
                    messages.error(request, "No hay artistas con email para este evento.")
                    return redirect("/admin/eventos/evento/")

                email = EmailMessage(
                    subject=f"Información sobre el evento: {evento.nombre}",
                    body=f"Hola, tienes una actualización sobre el evento '{evento.nombre}'.",
                    from_email="tu-email@ejemplo.com",
                    to=emails,
                )

                # Adjuntar los archivos seleccionados
                for archivo in archivos:
                    email.attach(archivo.name, archivo.read(), archivo.content_type)

                email.send(fail_silently=False)
                messages.success(request, "Email enviado correctamente.")
            except Exception as e:
                messages.error(request, f"Error al enviar el email: {e}")

            return redirect(f"/admin/eventos/evento/{evento_id}/change/")

