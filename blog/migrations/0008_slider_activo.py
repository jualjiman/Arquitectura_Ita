# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='activo',
            field=models.BooleanField(default=True, help_text=b'Debera ser mostrado?'),
            preserve_default=True,
        ),
    ]
