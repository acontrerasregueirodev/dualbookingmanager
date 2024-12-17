from django.urls import path
from . import views

urlpatterns = [
    # URL para ver todos los DJs
    path('djs/', views.ver_djs, name='ver_djs'),
    
    # URL para ver un DJ específico
    path('djs/<int:pk>/', views.ver_dj, name='ver_dj'),

    # URL para ver todos los managers
    path('managers/', views.ver_managers, name='ver_managers'),
    
    # URL para ver un manager específico
    path('managers/<int:pk>/', views.ver_manager, name='ver_manager'),

    # URL para ver todos los eventos
    path('eventos/', views.ver_eventos, name='ver_eventos'),
    
    # URL para ver un evento específico
    path('eventos/<int:pk>/', views.ver_evento, name='ver_evento'),

    # URL para ver todas las fotos de los DJs
    path('fotos/', views.ver_fotos, name='ver_fotos'),

    # URL para ver todas las documentaciones relacionadas con un DJ
    path('documentos/', views.ver_documentos, name='ver_documentos'),
]

