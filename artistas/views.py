from django.shortcuts import render, get_object_or_404
from .models import DJ, Manager, Evento, Foto, Documento

# Vista para ver todos los DJs
def ver_djs(request):
    djs = DJ.objects.all()
    return render(request, 'djs/ver_djs.html', {'djs': djs})

# Vista para ver un DJ específico
def ver_dj(request, pk):
    dj = get_object_or_404(DJ, pk=pk)
    return render(request, 'djs/ver_dj.html', {'dj': dj})

# Vista para ver todos los Managers
def ver_managers(request):
    managers = Manager.objects.all()
    return render(request, 'djs/ver_managers.html', {'managers': managers})

# Vista para ver un Manager específico
def ver_manager(request, pk):
    manager = get_object_or_404(Manager, pk=pk)
    return render(request, 'djs/ver_manager.html', {'manager': manager})

# Vista para ver todos los eventos
def ver_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'djs/ver_eventos.html', {'eventos': eventos})

# Vista para ver un evento específico
def ver_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    return render(request, 'djs/ver_evento.html', {'evento': evento})

# Vista para ver todas las fotos de los DJs
def ver_fotos(request):
    fotos = Foto.objects.all()
    return render(request, 'djs/ver_fotos.html', {'fotos': fotos})

# Vista para ver todos los documentos relacionados con los DJs
def ver_documentos(request):
    documentos = Documento.objects.all()
    return render(request, 'djs/ver_documentos.html', {'documentos': documentos})
