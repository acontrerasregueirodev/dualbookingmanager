"""
URL configuration for manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect



urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', lambda request: redirect('/admin/')),  # Redirigir la raíz a /admin
    path('panel/', include('panel.urls')),  # Las rutas de la app dashboard
    path('artistas/', include('artistas.urls')),  # Asegúrate de incluir las URLs de la app 'djs'
    #path('mailing/', include('mailing.urls')),  # Agregar la URL de la app mailing

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
