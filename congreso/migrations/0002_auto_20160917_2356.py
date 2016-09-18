# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('congreso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Obra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', models.ImageField(help_text=b'Imagen de obra del conferencista.', upload_to=b'obras')),
                ('contenido', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.AlterField(
            model_name='conferencista',
            name='imagen',
            field=models.ImageField(help_text=b'Imagen del conferencista.', upload_to=b'conferencistas'),
        ),
        migrations.AddField(
            model_name='obra',
            name='conferencista',
            field=models.ForeignKey(to='congreso.Conferencista'),
        ),
    ]
