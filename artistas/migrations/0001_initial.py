# Generated by Django 5.1.4 on 2024-12-17 02:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DJ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido_1', models.CharField(max_length=255)),
                ('apellido_2', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('tarifa_hora', models.DecimalField(decimal_places=2, max_digits=8)),
                ('experiencia', models.IntegerField()),
                ('genero_musical', models.CharField(max_length=255)),
                ('activo', models.BooleanField(default=True)),
                ('disponibilidad', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('fecha_evento', models.DateField()),
                ('lugar', models.CharField(max_length=255)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido_1', models.CharField(max_length=255)),
                ('apellido_2', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivo', models.FileField(upload_to='djs/documentos/')),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
                ('dj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documentos', to='artistas.dj')),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documentos', to='artistas.evento')),
            ],
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
                ('foto_url', models.URLField()),
                ('dj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fotos', to='artistas.dj')),
            ],
        ),
        migrations.AddField(
            model_name='dj',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='djs', to='artistas.manager'),
        ),
    ]
