# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('congreso', '0010_auto_20171017_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrocongreso',
            name='es_alumno_ITA',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='registrocurso',
            name='es_alumno_ITA',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='registromesasdedebate',
            name='es_alumno_ITA',
            field=models.BooleanField(default=False),
        ),
    ]
