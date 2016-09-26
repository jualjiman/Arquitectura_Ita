# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('congreso', '0005_registrocongreso_registrocurso_registromesasdedebate'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrocongreso',
            name='clave_de_registro',
            field=models.CharField(default='00000000', unique=True, max_length=8, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registrocongreso',
            name='es_valido',
            field=models.BooleanField(default='00000000'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registrocurso',
            name='clave_de_registro',
            field=models.CharField(default='00000000', unique=True, max_length=8, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registrocurso',
            name='es_valido',
            field=models.BooleanField(default='00000000'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registromesasdedebate',
            name='clave_de_registro',
            field=models.CharField(default='00000000', unique=True, max_length=8, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registromesasdedebate',
            name='es_valido',
            field=models.BooleanField(default='00000000'),
            preserve_default=False,
        ),
    ]
