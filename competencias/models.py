from django.db import models

class Competencia(models.Model):
    nombre_competencia=models.CharField(max_length=100) # Nombre de la competencia
    nivel = models.IntegerField()  # Nivel de la competencia
    atleta = models.CharField(max_length=100)  # Nombre del atleta
    club = models.CharField(max_length=100)  # Nombre del club
    puntuacion_ml = models.FloatField(null=True, blank=True)  # Puntuación ML
    puntuacion_db = models.FloatField(null=True, blank=True)  # Puntuación DB
    puntuacion_da = models.FloatField(null=True, blank=True)  # Puntuación DA
    puntuacion_e = models.FloatField(null=True, blank=True)  # Puntuación E
    puntuacion_art = models.FloatField(null=True, blank=True)  # Puntuación ART
    penalizacion = models.FloatField(null=True, blank=True)  # Penalización
    nota_final = models.FloatField()  # Nota final
    fecha = models.DateField()  # Fecha del evento
    aparato = models.CharField(max_length=20, choices=[
        ('Manos Libres', 'Manos Libres'),
        ('Aro', 'Aro'),
        ('Pelota', 'Pelota'),
        ('Cuerda', 'Cuerda'),
        ('Cinta', 'Cinta'),
        ('Masas', 'Masas'),
    ], default='Manos Libres')  # Establece un valor predeterminado


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_usuario = models.CharField(max_length=10, choices=[('Juez', 'Juez'), ('Padre', 'Padre')])
    club = models.CharField(max_length=100)
