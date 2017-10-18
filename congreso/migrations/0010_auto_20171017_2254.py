# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('congreso', '0009_auto_20161004_2149'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registrocongreso',
            options={'verbose_name': 'Registro de congreso', 'verbose_name_plural': 'Registros de congreso'},
        ),
        migrations.AlterModelOptions(
            name='registrocurso',
            options={'verbose_name': 'Registro de curso', 'verbose_name_plural': 'Registros de curso'},
        ),
        migrations.AlterModelOptions(
            name='registromesasdedebate',
            options={'verbose_name': 'Registro de mesas de debate', 'verbose_name_plural': 'Registros de mesas de debate'},
        ),
        migrations.AddField(
            model_name='registrocongreso',
            name='numero_control',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='registrocurso',
            name='numero_control',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='registromesasdedebate',
            name='numero_control',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='registrocongreso',
            name='estado_municipio',
            field=models.CharField(max_length=50, verbose_name=b'Estado y Municipio de Procedencia'),
        ),
        migrations.AlterField(
            model_name='registrocongreso',
            name='folio_recibo_oficial',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='registrocongreso',
            name='tipo_de_inscripcion',
            field=models.CharField(max_length=5, choices=[(b'esita', 'Alumnos y Ex Alumnos ITA ($500.00)'), (b'eotra', 'Alumnos otras Instituciones ($700.00)'), (b'profe', 'Profesionistas y p\xfablico en general ($950.00)')]),
        ),
        migrations.AlterField(
            model_name='registrocurso',
            name='estado_municipio',
            field=models.CharField(max_length=50, verbose_name=b'Estado y Municipio de Procedencia'),
        ),
        migrations.AlterField(
            model_name='registrocurso',
            name='folio_recibo_oficial',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='registromesasdedebate',
            name='estado_municipio',
            field=models.CharField(max_length=50, verbose_name=b'Estado y Municipio de Procedencia'),
        ),
        migrations.AlterField(
            model_name='registromesasdedebate',
            name='folio_recibo_oficial',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
