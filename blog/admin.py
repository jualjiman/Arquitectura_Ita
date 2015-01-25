from django.contrib import admin
from .models import Entrada,Slider
from easy_thumbnails.files import get_thumbnailer




# Register your models here.

class EntradaAdmin(admin.ModelAdmin):
		list_display = ('titulo','imagen', 'time')
		list_filter = ('time',)

		def img_publicacion(self,model_instance):
			return "<img src ='%s' />" % (get_thumbnailer(model_instance.imagen).url,)

		

class SliderAdmin(admin.ModelAdmin):
	list_display= ('titulo','imagen')
	list_filter = ('titulo',)





admin.site.register(Slider, SliderAdmin)
admin.site.register(Entrada,EntradaAdmin)

