from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Artista, Foto, Documento
from django.urls import reverse_lazy

# Vista para listar los artistas
class ArtistaListView(ListView):
    model = Artista
    template_name = 'artistas/artistas.html'

# Vista para ver los detalles de un artista
class ArtistaDetailView(DetailView):
    model = Artista
    template_name = 'artistas/artista_detail.html'

# Vista para crear un nuevo artista
class ArtistaCreateView(CreateView):
    model = Artista
    template_name = 'artistas/artista_form.html'
    fields = ['nombre', 'apellido_1', 'apellido_2', 'nombre_artistico', 'direccion', 'telefono', 'email', 'tarifa_hora', 'experiencia', 'activo', 'disponibilidad']

# Vista para editar un artista existente
class ArtistaUpdateView(UpdateView):
    model = Artista
    template_name = 'artistas/artista_form.html'
    fields = ['nombre', 'apellido_1', 'apellido_2', 'nombre_artistico', 'direccion', 'telefono', 'email', 'tarifa_hora', 'experiencia', 'activo', 'disponibilidad']

# Vista para eliminar un artista
class ArtistaDeleteView(DeleteView):
    model = Artista
    template_name = 'artistas/artista_confirm_delete.html'
    success_url = reverse_lazy('artista-list')

# Vistas para manejar fotos
class FotoListView(ListView):
    model = Foto
    template_name = 'artistas/foto_list.html'

class FotoCreateView(CreateView):
    model = Foto
    template_name = 'artistas/foto_form.html'
    fields = ['descripcion', 'foto_url']

# Vistas para manejar documentos
class DocumentoListView(ListView):
    model = Documento
    template_name = 'artistas/documento_list.html'

class DocumentoCreateView(CreateView):
    model = Documento
    template_name = 'artistas/documento_form.html'
    fields = ['titulo', 'descripcion', 'archivo']
