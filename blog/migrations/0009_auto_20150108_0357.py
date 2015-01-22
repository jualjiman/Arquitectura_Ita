# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_slider_activo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entrada',
            options={'ordering': None},
        ),
        migrations.AlterField(
            model_name='slider',
            name='activo',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
