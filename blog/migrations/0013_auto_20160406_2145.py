# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_slider_activo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semblanza',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', models.ImageField(help_text=b'Imagen del maestro.', upload_to=b'semblanzas')),
                ('nombre', models.CharField(max_length=100)),
                ('contenido', ckeditor.fields.RichTextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='imagen',
            field=models.ImageField(help_text=b'Imagen de la noticia', upload_to=b'imagenes'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entrada',
            name='resumen',
            field=models.CharField(help_text=b'Resumen de la noticia maximo 170 caracteres', max_length=170),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entrada',
            name='titulo',
            field=models.CharField(help_text=b'Titulo de la noticia maximo 100 caracteres', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='slider',
            name='activo',
            field=models.BooleanField(default=True, help_text=b'Mostrar o no la imagen con texto'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='slider',
            name='imagen',
            field=models.ImageField(help_text=b'Imagen que sera mostrada', upload_to=b'noticias'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='slider',
            name='titulo',
            field=models.CharField(help_text=b'Titulo que sera mostrado en la imagen, maximo 50 caracteres', max_length=50),
            preserve_default=True,
        ),
    ]
