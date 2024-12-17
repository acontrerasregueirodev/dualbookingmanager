from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('', views.listar_clientes, name='listar_clientes'),
    path('agregar/', views.agregar_cliente, name='agregar_cliente'),
]
