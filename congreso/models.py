# -*- coding: utf-8 -*-
from ckeditor.fields import RichTextField

from django.db import models
from django.template.defaultfilters import slugify


class Curso(models.Model):
    imagen = models.ImageField(
        upload_to='cursos',
        help_text='Imagen de curso/taller.'
    )
    nombre = models.CharField(
        max_length=150
    )
    contenido = RichTextField()
    activo = models.BooleanField(
        default=True
    )
    slug = models.SlugField(
        editable=False,
        max_length=150
    )

    def __unicode__(self):
        return u'{}'.format(self.nombre)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre.encode('utf-8'))
        super(Curso, self).save(*args, **kwargs)


class Conferencista(models.Model):
    imagen = models.ImageField(
        upload_to='conferencistas',
        help_text='Imagen del conferencista.'
    )
    nombre = models.CharField(
        max_length=100
    )
    contenido = RichTextField()
    activo = models.BooleanField(
        default=True
    )
    slug = models.SlugField(
        editable=False,
        max_length=150
    )

    def __unicode__(self):
        return u'{}'.format(self.nombre)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre.encode('utf-8'))
        super(Conferencista, self).save(*args, **kwargs)


class Obra(models.Model):
    """
    Obra correspondiente a un conferencista.
    """
    imagen = models.ImageField(
        upload_to='obras',
        help_text='Imagen de obra del conferencista.'
    )
    contenido = RichTextField()

    conferencista = models.ForeignKey(
        Conferencista,
        related_name='obras'
    )

    def __unicode__(self):
        return u'{}'.format(self.nombre)
