# urls.py en la app gestion_managers

from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_manager, name='crear_manager'),
    path('managers/', views.ver_managers, name='ver_managers'),
]