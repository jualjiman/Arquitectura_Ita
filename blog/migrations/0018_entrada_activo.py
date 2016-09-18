# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20160915_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]
