# contacto/utils.py

from django.core.mail import send_mail

def enviar_correo():
    subject = 'Asunto del correo'
    message = 'Este es el contenido del correo'
    recipient_list = ['destinatario@example.com']
    
    send_mail(
        subject,  # Asunto
        message,  # Cuerpo del mensaje
        'noreply@tuempresa.com',  # Remitente
        recipient_list,  # Lista de destinatarios
        fail_silently=False  # Si falla el envío, genera una excepción
    )
