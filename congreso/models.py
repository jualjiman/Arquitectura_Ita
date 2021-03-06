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
    dias_horario = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text=u'Dias y horario en los que se impartirá el curso.'
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


class BaseRegister(models.Model):
    """
    Modelo base, usado para los registros del congreso.
    """
    nombre = models.CharField(
        max_length=100
    )
    apellido_paterno = models.CharField(
        max_length=50
    )
    apellido_materno = models.CharField(
        max_length=50
    )
    numero_control = models.IntegerField(
        blank=True,
        null=True
    )
    correo_electronico = models.EmailField()
    escuela_de_procedencia = models.CharField(
        max_length=50
    )

    es_alumno_ITA = models.BooleanField(default=False)
    folio_recibo_oficial = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    estado_municipio = models.CharField(
        max_length=50,
        verbose_name="Estado y Municipio de Procedencia"
    )
    clave_de_registro = models.CharField(
        max_length=8,
        unique=True,
        editable=False
    )
    es_valido = models.BooleanField(
        blank=True,
        default=False
    )

    @property
    def nombre_completo(self):
        return u' '.join([
            self.nombre,
            self.apellido_paterno,
            self.apellido_materno,
        ])

    def __unicode__(self):
        return u'Registro de {}'.format(self.nombre_completo)

    class Meta:
        abstract = True


class RegistroCurso(BaseRegister):
    """
    Formulario de registro para cursos-taller.
    """
    curso = models.ForeignKey(Curso)

    class Meta:
        verbose_name = u'Registro de curso'
        verbose_name_plural = u'Registros de curso'


class RegistroCongreso(BaseRegister):
    """
    Formulario de registro para el congreso.
    """
    TIPOS_INSCRIPCION = (
        ('esita', u'Alumnos y Ex Alumnos ITA ($500.00)'),
        ('eotra', u'Alumnos otras Instituciones ($700.00)'),
        ('profe', u'Profesionistas y público en general ($950.00)'),
    )
    tipo_de_inscripcion = models.CharField(
        max_length=5,
        choices=TIPOS_INSCRIPCION,
    )

    class Meta:
        verbose_name = u'Registro de congreso'
        verbose_name_plural = u'Registros de congreso'


class RegistroMesasDeDebate(BaseRegister):
    """
    Formulario de registro para las mesas de debate.
    """
    archivo_sintesis = models.FileField(
        upload_to='archivosintesis',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = u'Registro de mesas de debate'
        verbose_name_plural = u'Registros de mesas de debate'
