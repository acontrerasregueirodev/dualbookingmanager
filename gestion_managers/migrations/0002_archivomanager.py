# Generated by Django 5.1.4 on 2024-12-17 01:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_managers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivoManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('archivo', models.FileField(upload_to='archivos_managers/')),
                ('fecha_subida', models.DateTimeField(auto_now_add=True)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='archivos', to='gestion_managers.manager')),
            ],
        ),
    ]