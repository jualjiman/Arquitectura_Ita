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
    slug = models.SlugField(editable=False)

    class Meta:
        ordering = ['-time']

    def __unicode__(self):
            return self.titulo

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(Entrada, self).save(*args, **kwargs)


class Slider(models.Model):
    imagen = models.ImageField(
        upload_to='noticias',
        help_text="Imagen que sera mostrada"
    )
    titulo = models.CharField(
        max_length=50,
        help_text="Titulo que sera mostrado en la imagen, maximo 50 caracteres"
    )
    activo = models.BooleanField(
        default=True,
        help_text="Mostrar o no la imagen con texto"
    )

    def __unicode__(self):
        return self.titulo


class Semblanza(models.Model):
    imagen = models.ImageField(
        upload_to='semblanzas',
        help_text='Imagen del maestro.'
    )
    nombre = models.CharField(
        max_length=100
    )
    contenido = RichTextField()
    slug = models.SlugField(editable=False)

    def __unicode__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Semblanza, self).save(*args, **kwargs)
