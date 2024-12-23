# mailing/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('enviar-correo/', views.enviar_correo_admin, name='enviar_correo_admin'),
]
