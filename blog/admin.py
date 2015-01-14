from django.contrib import admin
from .models import Entrada,Slider
from sorl.thumbnail.admin import AdminImageMixin



# Register your models here.

class EntradaAdmin(admin.ModelAdmin):
		list_display = ('titulo','imagen', 'time')
		list_filter = ('titulo','time')

class SliderAdmin(admin.ModelAdmin):
	list_display= ('titulo','imagen')



admin.site.register(Slider, SliderAdmin)
admin.site.register(Entrada,EntradaAdmin)

