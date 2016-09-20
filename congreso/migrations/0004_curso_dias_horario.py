# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('congreso', '0003_auto_20160918_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='dias_horario',
            field=models.CharField(help_text='Dias y horario en los que se impartir\xe1 el curso.', max_length=200, null=True, blank=True),
        ),
    ]
