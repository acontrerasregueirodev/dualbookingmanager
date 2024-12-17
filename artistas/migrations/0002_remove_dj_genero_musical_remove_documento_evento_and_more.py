# Generated by Django 5.1.4 on 2024-12-17 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artistas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dj',
            name='genero_musical',
        ),
        migrations.RemoveField(
            model_name='documento',
            name='evento',
        ),
        migrations.AddField(
            model_name='dj',
            name='nombre_artistico',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]