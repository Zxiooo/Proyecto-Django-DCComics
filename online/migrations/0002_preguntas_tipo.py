# Generated by Django 5.1 on 2024-10-28 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='preguntas',
            name='Tipo',
            field=models.CharField(choices=[('Pelicula', 'Pelicula'), ('Serie', 'Serie')], default='Pelicula', help_text='Pelicula o Serie', max_length=20),
        ),
    ]
