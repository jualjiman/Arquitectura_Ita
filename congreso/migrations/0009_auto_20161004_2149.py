# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('congreso', '0008_auto_20160929_2240'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registrocongreso',
            options={'verbose_name': 'Registros de congreso'},
        ),
        migrations.AlterModelOptions(
            name='registrocurso',
            options={'verbose_name': 'Registros de curso'},
        ),
        migrations.AlterModelOptions(
            name='registromesasdedebate',
            options={'verbose_name': 'Registros de mesas de debate'},
        ),
    ]
