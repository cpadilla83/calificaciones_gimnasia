from django.shortcuts import render, redirect
from .models import Competencia
from datetime import date

def ingresar_calificacion(request):
    if request.method == 'POST':
        competencia = Competencia(
            nombre_competencia=request.POST.get('nombre_competencia') or None,
            nivel=request.POST.get('nivel') or None,  # Usar None si está vacío
            atleta=request.POST.get('atleta'),  # Asumimos que atleta es obligatorio
            club=request.POST.get('club'),  # Asumimos que club es obligatorio
            puntuacion_ml=request.POST.get('puntuacion_ml') or None,
            puntuacion_db=request.POST.get('puntuacion_db') or None,
            puntuacion_da=request.POST.get('puntuacion_da') or None,
            puntuacion_e=request.POST.get('puntuacion_e') or None,
            puntuacion_art=request.POST.get('puntuacion_art') or None,
            penalizacion=request.POST.get('penalizacion') or None,
            nota_final=request.POST.get('nota_final') or None,
            fecha=request.POST.get('fecha'),
            aparato=request.POST.get('aparato') or None,  # Campo aparato
        )
        competencia.save()
        return redirect('competencias:ver_calificaciones')  # Asegúrate de usar el namespace
    return render(request, 'competencias/ingresar_calificacion.html')


def ver_calificaciones(request):
    calificaciones = Competencia.objects.all().order_by('-fecha')
    return render(request, 'competencias/ver_calificaciones.html', {'calificaciones': calificaciones})
