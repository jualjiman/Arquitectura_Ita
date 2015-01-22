# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_remove_slider_activo'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='activo',
            field=models.BooleanField(default=True, help_text=b'Debera ser mostrado?'),
            preserve_default=True,
        ),
    ]
