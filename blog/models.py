from django.db import models
from django.contrib import admin
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from sorl.thumbnail import ImageField


#from tinymce import models as tinymce_models
from django.conf import global_settings
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)
BOOTSTRAP_ADMIN_SIDEBAR_MENU = True

# Create your models here.
class Entrada(models.Model):
	imagen = models.ImageField(upload_to = 'imagenes')
	titulo = models.CharField(max_length=100)
	resumen = models.CharField(max_length=170)
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
		super(Entrada, self).save( *args, **kwargs)

	def get_query_set (self):
		return super(Entrada, self).get_query_set()[:3]


	
		



class Slider(models.Model):
	imagen = models.ImageField(upload_to= 'noticias')
	titulo = models.CharField(max_length=50)
	
	












