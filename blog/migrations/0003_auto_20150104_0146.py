# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_entrada_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='titulo',
            field=models.CharField(max_length=144),
            preserve_default=True,
        ),
    ]
