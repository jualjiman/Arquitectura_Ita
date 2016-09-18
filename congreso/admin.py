# -*- coding: utf-8 -*-
from django.contrib import admin

from sorl.thumbnail.shortcuts import get_thumbnail

from .models import Conferencista, Curso, Obra


class CursoAdmin(admin.ModelAdmin):
    list_display = (
        'imagen_curso',
        'nombre',
        'activo',
    )

    def imagen_curso(self, instance):
        return (
            '<img src="{}" />'.format(
                get_thumbnail(
                    instance.imagen,
                    "100x100",
                    crop="center"
                ).url
            )
        )
    imagen_curso.allow_tags = True


class ObraInline(admin.StackedInline):
    model = Obra
    extra = 0


class ConferencistaAdmin(admin.ModelAdmin):
    inlines = [ObraInline, ]
    list_display = (
        'imagen_conferencista',
        'nombre',
        'activo',
    )

    def imagen_conferencista(self, instance):
        return (
            '<img src="{}" />'.format(
                get_thumbnail(
                    instance.imagen,
                    "100x100",
                    crop="center"
                ).url
            )
        )
    imagen_conferencista.allow_tags = True

admin.site.register(Curso, CursoAdmin)
admin.site.register(Conferencista, ConferencistaAdmin)
