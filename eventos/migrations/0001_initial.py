# Generated by Django 5.1.4 on 2024-12-23 16:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('fecha', models.DateField()),
                ('fecha_fin', models.DateField(blank=True, null=True)),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('direccion', models.CharField(max_length=255)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('confirmado', 'Confirmado'), ('cancelado', 'Cancelado')], default='pendiente', max_length=20)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eventos', to='clientes.cliente')),
            ],
        ),
    ]