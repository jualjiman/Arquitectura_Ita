# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('congreso', '0006_auto_20160924_2249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrocongreso',
            old_name='es_alumno_ita',
            new_name='es_alumno_ITA',
        ),
        migrations.RenameField(
            model_name='registrocurso',
            old_name='es_alumno_ita',
            new_name='es_alumno_ITA',
        ),
        migrations.RenameField(
            model_name='registromesasdedebate',
            old_name='es_alumno_ita',
            new_name='es_alumno_ITA',
        ),
        migrations.AlterField(
            model_name='registrocongreso',
            name='es_valido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='registrocurso',
            name='es_valido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='registromesasdedebate',
            name='es_valido',
            field=models.BooleanField(default=False),
        ),
    ]
