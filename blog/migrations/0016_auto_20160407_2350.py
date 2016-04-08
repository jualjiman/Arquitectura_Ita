# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_semblanza_activo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivoPublicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcionArchivo', models.CharField(help_text=b'Texto descriptivo del archivo.', max_length=60)),
                ('archivo', models.FileField(help_text='Archivo asociado con la publicacion', upload_to=b'pdfpublicacion')),
                ('publicacion', models.ForeignKey(to='blog.Entrada')),
            ],
            options={
                'verbose_name_plural': 'Archivo de publicaci\xf3n',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VideoPublicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcionVideoYoutube', models.CharField(help_text=b'Texto descriptivo del video de youtube.', max_length=60)),
                ('claveYoutube', models.CharField(help_text=b'Clave de video de youtube asociado con la publicacion', max_length=20)),
                ('publicacion', models.ForeignKey(to='blog.Entrada')),
            ],
            options={
                'verbose_name_plural': 'Videos de publicacion',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='slider',
            name='imagen',
            field=models.ImageField(help_text='Imagen que ser\xe1 mostrada', upload_to=b'noticias'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='slider',
            name='titulo',
            field=models.CharField(help_text='Titulo que ser\xe1 mostrado en la imagen, maximo 50 caracteres', max_length=50),
            preserve_default=True,
        ),
    ]
