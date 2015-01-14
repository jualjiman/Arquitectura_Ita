# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20150108_0357'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entrada',
            options={'ordering': ['-time']},
        ),
    ]
