# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', models.ImageField(upload_to=b'photos')),
                ('titulo', models.CharField(max_length=100)),
                ('resumen', models.CharField(max_length=150)),
                ('contenido', models.TextField()),
                ('time', models.DateTimeField()),
                ('slug', models.SlugField(editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
