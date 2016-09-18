# -*- coding: utf-8 -*-
from ckeditor.fields import RichTextField

from django.db import models
from django.template.defaultfilters import slugify


class Entrada(models.Model):
    imagen = models.ImageField(
        upload_to='imagenes',
        help_text="Imagen de la noticia"
    )
    titulo = models.CharField(
        max_length=100,
        help_text="Titulo de la noticia maximo 100 caracteres"
    )
    resumen = models.CharField(
        max_length=170,
        help_text="Resumen de la noticia maximo 170 caracteres"
    )
    contenido = RichTextField()
    time = models.DateTimeField()
    slug = models.SlugField(
        editable=False,
        max_length=150
    )

    @property
    def videos(self):
        return VideoPublicacion.objects.filter(publicacion=self)

    @property
    def archivos(self):
        return ArchivoPublicacion.objects.filter(publicacion=self)

    class Meta:
        ordering = ['-time']

    def __unicode__(self):
        return u'{}'.format(self.titulo)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo.encode('utf-8'))
        super(Entrada, self).save(*args, **kwargs)


class VideoPublicacion(models.Model):
    class Meta:
        verbose_name_plural = "Videos de publicacion"

    descripcionVideoYoutube = models.CharField(
        max_length=60,
        help_text="Texto descriptivo del video de youtube."
    )
    claveYoutube = models.CharField(
        max_length=20,
        help_text='Clave de video de youtube asociado con la publicacion'
    )
    publicacion = models.ForeignKey(Entrada)


class ArchivoPublicacion(models.Model):
    class Meta:
        verbose_name_plural = u'Archivo de publicación'
    descripcionArchivo = models.CharField(
        max_length=60,
        help_text="Texto descriptivo del archivo."
    )
    archivo = models.FileField(
        upload_to="pdfpublicacion",
        help_text=u'Archivo asociado con la publicacion'
    )
    publicacion = models.ForeignKey(Entrada)


class Slider(models.Model):
    imagen = models.ImageField(
        upload_to='noticias',
        help_text=u'Imagen que será mostrada'
    )
    titulo = models.CharField(
        max_length=50,
        help_text=(
            u'Titulo que será mostrado en la imagen, maximo 50 caracteres'
        )
    )
    activo = models.BooleanField(
        default=True,
        help_text="Mostrar o no la imagen con texto"
    )

    def __unicode__(self):
        return u'{}'.format(self.titulo)


class Semblanza(models.Model):
    imagen = models.ImageField(
        upload_to='semblanzas',
        help_text='Imagen del maestro.'
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
        super(Semblanza, self).save(*args, **kwargs)
