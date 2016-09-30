# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('congreso', '0007_auto_20160925_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrocongreso',
            name='folio_recibo_oficial',
            field=models.CharField(help_text='S\xf3lo alumnos ITA', max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='registrocongreso',
            name='tipo_de_inscripcion',
            field=models.CharField(max_length=5, choices=[(b'esita', 'Estudiantes ITA ($500.00)'), (b'eotra', 'Estudiantes de otra instituci\xf3n ($600.00)'), (b'egres', 'Egresados ITA ($700.00)'), (b'profe', 'Profesionistas ($1,000.00)')]),
        ),
        migrations.AlterField(
            model_name='registrocurso',
            name='folio_recibo_oficial',
            field=models.CharField(help_text='S\xf3lo alumnos ITA', max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='registromesasdedebate',
            name='folio_recibo_oficial',
            field=models.CharField(help_text='S\xf3lo alumnos ITA', max_length=50, null=True, blank=True),
        ),
    ]
