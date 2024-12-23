# Generated by Django 5.1.4 on 2024-12-23 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_evento', models.CharField(help_text='Nombre del lugar o evento', max_length=255, verbose_name='Nombre de la discoteca o festival')),
                ('direccion', models.TextField(help_text='Dirección completa del lugar del evento', verbose_name='Dirección de la sala')),
                ('persona_contacto', models.CharField(help_text='Nombre completo de la persona de contacto', max_length=255, verbose_name='Persona de contacto')),
                ('telefono', models.CharField(blank=True, max_length=15, null=True, verbose_name='Teléfono de contacto')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Correo electrónico de contacto')),
                ('notas', models.TextField(blank=True, help_text='Cualquier información adicional relevante sobre el cliente', verbose_name='Notas adicionales')),
                ('otros_datos', models.JSONField(blank=True, help_text='Campo flexible para almacenar información adicional', null=True, verbose_name='Otros datos')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('ultima_modificacion', models.DateTimeField(auto_now=True, verbose_name='Última modificación')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['-fecha_creacion'],
            },
        ),
    ]
