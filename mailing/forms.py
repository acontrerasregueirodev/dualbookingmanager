# contacto/forms.py

from django import forms

class CorreoForm(forms.Form):
    subject = forms.CharField(max_length=200, label='Asunto')
    message = forms.CharField(widget=forms.Textarea, label='Mensaje')
    recipient_list = forms.CharField(widget=forms.Textarea, label='Destinatarios (separados por comas)')
