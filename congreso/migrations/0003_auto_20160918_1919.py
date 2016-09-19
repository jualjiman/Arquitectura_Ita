# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('congreso', '0002_auto_20160917_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obra',
            name='conferencista',
            field=models.ForeignKey(related_name='obras', to='congreso.Conferencista'),
        ),
    ]
