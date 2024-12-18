from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('artistas/', include('artistas.urls')),  # Asegúrate de que 'name' sea 'artistas'

]