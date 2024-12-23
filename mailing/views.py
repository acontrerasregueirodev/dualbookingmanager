# contacto/views.py

from django.core.mail import send_mail
from django.shortcuts import render
from .forms import CorreoForm

def enviar_correo_admin(request):
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
            # Después de enviar el correo, puedes redirigir o mostrar un mensaje de éxito
            return render(request, 'correo_enviado.html')  # Página de éxito
    else:
        form = CorreoForm()

    return render(request, 'enviar_correo.html', {'form': form})
