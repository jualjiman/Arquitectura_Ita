from django.contrib import admin

from easy_thumbnails.files import get_thumbnailer

from .models import Entrada, Semblanza, Slider


class EntradaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'img_publicacion', 'time')
    list_filter = ('time',)

    def img_publicacion(self, instance):
        options = {
            'size': (100, 66),
            'crop': True
        }
        return (
            '<img src="{}" />'.format(
                get_thumbnailer(instance.imagen).get_thumbnail(options).url
            )
        )
    img_publicacion.allow_tags = True


class SliderAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'imagen_slide')
    list_filter = ('titulo', )

    def imagen_slide(self, instance):
        options = {
            'size': (250, 100),
            'crop': True
        }
        return (
            '<img src="{}" />'.format(
                get_thumbnailer(instance.imagen).get_thumbnail(options).url
            )
        )
    imagen_slide.allow_tags = True


class SemblanzaAdmin(admin.ModelAdmin):
    list_display = ('imagen_maestro', 'nombre', )

    def imagen_maestro(self, instance):
        options = {
            'size': (100, 100),
            'crop': True
        }

        return (
            '<img src="{}" />'.format(
                get_thumbnailer(instance.imagen).get_thumbnail(options).url
            )
        )
    imagen_maestro.allow_tags = True


admin.site.register(Slider, SliderAdmin)
admin.site.register(Entrada, EntradaAdmin)
admin.site.register(Semblanza, SemblanzaAdmin)
