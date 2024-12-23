# contacto/admin.py

from django.contrib import admin
from django.core.mail import send_mail
from django.urls import path
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import CorreoForm
from .models import Evento

class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'fecha', 'estado')

    # Registrar una nueva URL para la acción personalizada
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('enviar-correo/', self.enviar_correo_admin),
        ]
        return custom_urls + urls

    def enviar_correo_admin(self, request):
        if request.method == 'POST':
            form = CorreoForm(request.POST)
            if form.is_valid():
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']
                recipient_list = form.cleaned_data['recipient_list'].split(',')
                
                send_mail(
                    subject,
                    message,
                    'noreply@tuempresa.com',  # Remitente
                    recipient_list,  # Lista de destinatarios
                    fail_silently=False
                )
                # Después de enviar el correo, redirige al admin
                self.message_user(request, "Correo enviado exitosamente.")
                return HttpResponseRedirect("..")
        else:
            form = CorreoForm()

        return render(request, 'admin/enviar_correo.html', {'form': form})

admin.site.register(Evento, EventoAdmin)

