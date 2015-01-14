# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150104_0147'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='imagen',
            field=models.ImageField(default=datetime.datetime(2015, 1, 4, 9, 19, 33, 820459, tzinfo=utc), upload_to=b'imagenes'),
            preserve_default=False,
        ),
    ]
