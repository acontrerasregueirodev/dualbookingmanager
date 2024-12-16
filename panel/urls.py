from django.urls import path
from panel import views

urlpatterns = [
    path('', views.panel, name='panel'),  # Vista protegida del dashboard
]