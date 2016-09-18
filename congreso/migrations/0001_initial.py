# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conferencista',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', models.ImageField(help_text=b'Imagen del maestro.', upload_to=b'semblanzas')),
                ('nombre', models.CharField(max_length=100)),
                ('contenido', ckeditor.fields.RichTextField()),
                ('activo', models.BooleanField(default=True)),
                ('slug', models.SlugField(max_length=150, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', models.ImageField(help_text=b'Imagen de curso/taller.', upload_to=b'cursos')),
                ('nombre', models.CharField(max_length=150)),
                ('contenido', ckeditor.fields.RichTextField()),
                ('activo', models.BooleanField(default=True)),
                ('slug', models.SlugField(max_length=150, editable=False)),
            ],
        ),
    ]
