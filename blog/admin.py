from django.contrib import admin
from .models import Entrada,Slider
from easy_thumbnails.files import get_thumbnailer




# Register your models here.

class EntradaAdmin(admin.ModelAdmin):
		list_display = ('titulo','img_publicacion', 'time')
		list_filter = ('time',)

		def img_publicacion(self,model_instance):

			options = {'size': (100, 66), 'crop': True}
			return ("<img src ='%s' />" % (get_thumbnailer(model_instance.imagen).get_thumbnail(options).url,) )
		img_publicacion.allow_tags= True
		

class SliderAdmin(admin.ModelAdmin):
	list_display= ('titulo','img_slider')
	list_filter = ('titulo',)


	def img_slider(self,model_instance):

		options = {'size': (250, 100), 'crop': True}
		return ("<img src ='%s' />" % (get_thumbnailer(model_instance.imagen).get_thumbnail(options).url,) )
	img_slider.allow_tags= True




admin.site.register(Slider, SliderAdmin)
admin.site.register(Entrada,EntradaAdmin)

