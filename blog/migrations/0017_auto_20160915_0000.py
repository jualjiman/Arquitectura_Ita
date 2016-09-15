# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20160407_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='slug',
            field=models.SlugField(max_length=150, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='semblanza',
            name='slug',
            field=models.SlugField(max_length=150, editable=False),
            preserve_default=True,
        ),
    ]
