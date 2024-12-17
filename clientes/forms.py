from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['razon_social', 'nombre', 'apellido_1', 'apellido_2', 'email', 'telefono', 
                  'cif', 'numero_cuenta', 'direccion', 'ciudad', 'provincia', 
                  'codigo_postal', 'telefono_contacto', 'email_contacto', 'activo']
