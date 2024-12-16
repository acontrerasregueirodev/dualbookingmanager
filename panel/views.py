# dashboard/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def panel(request):
    # Aquí puedes agregar datos que quieras mostrar en el dashboard
    return render(request, 'panel/panel.html')
