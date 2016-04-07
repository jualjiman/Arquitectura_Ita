# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20160406_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='semblanza',
            name='slug',
            field=models.SlugField(default='arq-federico-zagal-leon', editable=False),
            preserve_default=False,
        ),
    ]
