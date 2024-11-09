# Generated by Django 5.1 on 2024-10-22 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduloPeliculas', '0002_pelicula_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='tipo',
            field=models.CharField(choices=[('Pelicula', 'Pelicula'), ('Serie', 'Serie')], help_text='Pelicula o Serie', max_length=20),
        ),
    ]
