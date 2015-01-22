# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20150108_0408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slider',
            name='activo',
        ),
    ]
