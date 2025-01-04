from django.contrib import admin
from django.urls import path
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.utils.html import format_html
from django.contrib import messages
from .models import Evento

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
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
            'classes': ('wide', 'form-row'),  # Se añade 'form-row' para alineación
        }),
    )

    # Método para mostrar los nombres de los artistas asociados al evento
    def get_artistas(self, obj):
        return ", ".join([artista.nombre for artista in obj.artistas.all()])
    get_artistas.short_description = 'Artistas'

    # Método para mostrar el botón de enviar email
    def enviar_email(self, obj):
        return format_html('<a class="button" href="{}">Enviar Email</a>', f"{obj.id}/enviar-email/")
    enviar_email.short_description = 'Acción'
    enviar_email.allow_tags = True

    # Sobrescribir URLs del administrador para añadir una acción personalizada
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                '<int:evento_id>/enviar-email/',
                self.admin_site.admin_view(self.enviar_email_artistas),
                name='enviar_email_artistas',
            ),
        ]
        return custom_urls + urls


    def enviar_email_artistas(self, request, evento_id):
        try:
            evento = Evento.objects.get(id=evento_id)
            artistas = evento.artistas.all()
            emails = [artista.email for artista in artistas if artista.email]

            if not emails:
                messages.error(request, "No hay artistas con email para este evento.")
                return redirect("/admin/eventos/evento/")

            # Logging emails to verify recipients
            print(f"Sending email to: {emails}")

            send_mail(
                subject=f"Información sobre el evento: {evento.nombre}",
                message=f"Hola, tienes una actualización sobre el evento: {evento.nombre}.",
                from_email="8241b4001@smtp-brevo.com",  # Replace with your configured email
                recipient_list=emails,
                fail_silently=False,
            )
            messages.success(request, f"Correo enviado a los artistas del evento '{evento.nombre}'.")
        except Evento.DoesNotExist:
            messages.error(request, "Evento no encontrado.")
        except Exception as e:
            print(f"Error during email sending: {e}")  # Debugging
            messages.error(request, f"Error al enviar el correo: {e}")

        return redirect("/admin/eventos/evento/")
