# Generated by Django 5.1.4 on 2024-12-17 01:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(max_length=20)),
                ('calle', models.CharField(max_length=255)),
                ('ciudad', models.CharField(max_length=100)),
                ('estado', models.CharField(blank=True, max_length=100, null=True)),
                ('pais', models.CharField(max_length=100)),
                ('codigo_postal', models.CharField(max_length=20)),
                ('notas', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]