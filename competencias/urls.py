from django.urls import path
from . import views

app_name = 'competencias'  # Define el espacio de nombres aquí

urlpatterns = [
    path('ingresar/', views.ingresar_calificacion, name='ingresar_calificacion'),
    path('ver/', views.ver_calificaciones, name='ver_calificaciones'),
]
