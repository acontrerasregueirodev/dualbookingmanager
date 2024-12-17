# views.py en gestion_managers

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Manager
from .forms import ManagerForm  # Asegúrate de tener un formulario de Manager

def crear_manager(request):
    if request.method == 'POST':
        form = ManagerForm(request.POST)
        if form.is_valid():
            # Guardar el formulario pero no en la base de datos aún
            manager = form.save(commit=False)

            # Crear el usuario automáticamente
            user = User.objects.create_user(
                username=form.cleaned_data['email'],  # Usa el email como username
                email=form.cleaned_data['email'],
                password=form.cleaned_data['telefono']  # Usa el teléfono como contraseña
            )

            # Asignar el usuario al Manager
            manager.user = user

            # Ahora guarda el Manager en la base de datos
            manager.save()

            return redirect('ver_managers')  # Redirige a la lista de managers
    else:
        form = ManagerForm()

    return render(request, 'gestion_managers/crear_manager.html', {'form': form})

def ver_managers(request):
    # Cargar los managers y sus archivos
    managers = Manager.objects.all().prefetch_related('archivos')

    context = {
        'managers': managers
    }
    return render(request, 'gestion_managers/ver_manager.html', context)

