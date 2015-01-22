from django.db import models 
from django.contrib import admin
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField



#from tinymce import models as tinymce_models
from django.conf import global_settings
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)
BOOTSTRAP_ADMIN_SIDEBAR_MENU = True

# Create your models here.)
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

	
	
class Slider(models.Model):
	imagen = models.ImageField(upload_to= 'noticias')
	titulo = models.CharField(max_length=50)
	activo = models.BooleanField(default=True, help_text="Debera ser mostrado?")

	def __unicode__(self):
		return self.titulo
	
	












