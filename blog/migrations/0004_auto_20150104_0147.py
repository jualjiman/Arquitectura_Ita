# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150104_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='resumen',
            field=models.CharField(max_length=170),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entrada',
            name='titulo',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
