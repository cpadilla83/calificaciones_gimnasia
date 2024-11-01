# Generated by Django 5.1.2 on 2024-10-31 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Competencia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nivel", models.IntegerField()),
                ("atleta", models.CharField(max_length=100)),
                ("club", models.CharField(max_length=100)),
                ("puntuacion_ml", models.FloatField()),
                ("puntuacion_db", models.FloatField()),
                ("puntuacion_da", models.FloatField()),
                ("puntuacion_e", models.FloatField()),
                ("puntuacion_art", models.FloatField()),
                ("penalizacion", models.FloatField()),
                ("nota_final", models.FloatField()),
                ("fecha", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Usuario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                (
                    "tipo_usuario",
                    models.CharField(
                        choices=[("Juez", "Juez"), ("Padre", "Padre")], max_length=10
                    ),
                ),
                ("club", models.CharField(max_length=100)),
            ],
        ),
    ]