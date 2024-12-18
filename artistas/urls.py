from django.urls import path
from . import views

urlpatterns = [
    # Ruta para listar todos los artistas
    path('', views.ArtistaListView.as_view(), name='artista-list'),
    
    # Ruta para ver los detalles de un artista específico
    path('artistas/<int:pk>/', views.ArtistaDetailView.as_view(), name='artista-detail'),
    
    # Ruta para agregar un nuevo artista
    path('artistas/nuevo/', views.ArtistaCreateView.as_view(), name='artista-create'),
    
    # Ruta para editar un artista existente
    path('artistas/<int:pk>/editar/', views.ArtistaUpdateView.as_view(), name='artista-edit'),
    
    # Ruta para eliminar un artista
    path('artistas/<int:pk>/eliminar/', views.ArtistaDeleteView.as_view(), name='artista-delete'),

    # Rutas para fotos
    path('artistas/<int:artista_id>/fotos/', views.FotoListView.as_view(), name='foto-list'),
    path('artistas/<int:artista_id>/fotos/nueva/', views.FotoCreateView.as_view(), name='foto-create'),
    
    # Rutas para documentos
    path('artistas/<int:artista_id>/documentos/', views.DocumentoListView.as_view(), name='documento-list'),
    path('artistas/<int:artista_id>/documentos/nuevo/', views.DocumentoCreateView.as_view(), name='documento-create'),
]
