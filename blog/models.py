from ckeditor.fields import RichTextField

from django.conf import global_settings
from django.db import models
from django.template.defaultfilters import slugify


TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)
BOOTSTRAP_ADMIN_SIDEBAR_MENU = True


# Create your models here.)
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
        if not self.id:
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
