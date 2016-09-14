from django.contrib import admin

from sorl.thumbnail.shortcuts import get_thumbnail

from .models import (
    ArchivoPublicacion,
    Entrada,
    Semblanza,
    Slider,
    VideoPublicacion
)


class VideoInline(admin.StackedInline):
    model = VideoPublicacion
    extra = 0


class ArchivoInline(admin.StackedInline):
    model = ArchivoPublicacion
    extra = 0


class EntradaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'img_publicacion', 'time')
    list_filter = ('time',)
    inlines = [VideoInline, ArchivoInline, ]

    def img_publicacion(self, instance):
        return (
            '<img src="{}" />'.format(
                get_thumbnail(
                    instance.imagen,
                    "100x66",
                    crop="center"
                ).url
            )
        )
    img_publicacion.allow_tags = True


class SliderAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'imagen_slide')
    list_filter = ('titulo', )

    def imagen_slide(self, instance):
        return (
            '<img src="{}" />'.format(
                get_thumbnail(
                    instance.imagen,
                    "250x100",
                    crop="center"
                ).url
            )
        )
    imagen_slide.allow_tags = True


class SemblanzaAdmin(admin.ModelAdmin):
    list_display = ('imagen_maestro', 'nombre', )

    def imagen_maestro(self, instance):
        return (
            '<img src="{}" />'.format(
                get_thumbnail(
                    instance.imagen,
                    "100x100",
                    crop="center"
                ).url
            )
        )
    imagen_maestro.allow_tags = True


admin.site.register(Slider, SliderAdmin)
admin.site.register(Entrada, EntradaAdmin)
admin.site.register(Semblanza, SemblanzaAdmin)
