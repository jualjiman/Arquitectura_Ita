# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('congreso', '0004_curso_dias_horario'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroCongreso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido_paterno', models.CharField(max_length=50)),
                ('apellido_materno', models.CharField(max_length=50)),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('escuela_de_procedencia', models.CharField(max_length=50)),
                ('es_alumno_ita', models.BooleanField()),
                ('folio_recibo_oficial', models.CharField(max_length=50, null=True, blank=True)),
                ('estado_municipio', models.CharField(max_length=50)),
                ('tipo_de_inscripcion', models.CharField(max_length=5, choices=[(b'esita', 'Estudiantes ITA (%500.00)'), (b'eotra', 'Estudiantes de otra instituci\xf3n ($600.00)'), (b'egres', 'Egresados ITA ($700.00)'), (b'profe', 'Profesionistas ($1,000.00)')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RegistroCurso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido_paterno', models.CharField(max_length=50)),
                ('apellido_materno', models.CharField(max_length=50)),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('escuela_de_procedencia', models.CharField(max_length=50)),
                ('es_alumno_ita', models.BooleanField()),
                ('folio_recibo_oficial', models.CharField(max_length=50, null=True, blank=True)),
                ('estado_municipio', models.CharField(max_length=50)),
                ('curso', models.ForeignKey(to='congreso.Curso')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RegistroMesasDeDebate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido_paterno', models.CharField(max_length=50)),
                ('apellido_materno', models.CharField(max_length=50)),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('escuela_de_procedencia', models.CharField(max_length=50)),
                ('es_alumno_ita', models.BooleanField()),
                ('folio_recibo_oficial', models.CharField(max_length=50, null=True, blank=True)),
                ('estado_municipio', models.CharField(max_length=50)),
                ('archivo_sintesis', models.FileField(null=True, upload_to=b'archivosintesis', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
