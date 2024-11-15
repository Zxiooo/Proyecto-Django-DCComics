# Generated by Django 5.1 on 2024-10-27 20:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Preguntas',
            fields=[
                ('idPregunta', models.AutoField(primary_key=True, serialize=False)),
                ('Titulo', models.CharField(max_length=60)),
                ('Pregunta', models.TextField()),
                ('Fecha_creacion', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nombre', models.CharField(max_length=30, verbose_name='')),
                ('apellido', models.CharField(max_length=30, verbose_name='')),
                ('rut', models.CharField(max_length=12, unique=True, verbose_name='')),
                ('correo', models.EmailField(max_length=70, unique=True, verbose_name='')),
                ('usuario', models.CharField(max_length=50, unique=True, verbose_name='')),
                ('fecha_nacimiento', models.DateField(max_length=50, null=True, verbose_name='')),
                ('activo', models.BooleanField(default=True)),
                ('admin', models.BooleanField(default=False)),
                ('tecnico', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('idRespuesta', models.AutoField(primary_key=True, serialize=False)),
                ('Respuesta', models.TextField(verbose_name='')),
                ('FechaHora', models.DateTimeField()),
                ('id_Pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online.preguntas')),
                ('Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='preguntas',
            name='Usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online.usuario'),
        ),
    ]
