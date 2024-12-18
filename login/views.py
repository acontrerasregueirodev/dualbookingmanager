# login/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Autenticar al usuario
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Si las credenciales son correctas, iniciar sesión
            login(request, user)
            return redirect('artista-list')  # Redirigir a la página de inicio o al dashboard
        else:
            # Si las credenciales son incorrectas, mostrar un mensaje de error
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    
    return render(request, 'login/login.html')
def logout_view(request):
    logout(request)  # Esto cierra la sesión del usuario
    return redirect('login')  # Redirige al login después de hacer logout
