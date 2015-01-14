# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_entrada_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='contenido',
            field=ckeditor.fields.RichTextField(),
            preserve_default=True,
        ),
    ]
