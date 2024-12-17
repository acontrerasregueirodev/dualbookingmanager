# forms.py en la app gestion_managers

from django import forms
from .models import Manager

class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        exclude = ['user']  # Excluimos el campo 'user' porque lo asignaremos automáticamente
