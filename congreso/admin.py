# -*- coding: utf-8 -*-
from django.contrib import admin

from sorl.thumbnail.shortcuts import get_thumbnail

from .models import (
    Conferencista, Curso, Obra,
    RegistroCongreso, RegistroCurso, RegistroMesasDeDebate
)


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


class RegistroCursoAdmin(admin.ModelAdmin):
    list_display = (
        'clave_de_registro',
        'nombre',
        'apellido_paterno',
        'apellido_materno',
        'correo_electronico',
        'escuela_de_procedencia',
        'es_alumno_ITA',
        'curso',
    )
    search_fields = (
        'clave_de_registro',
        'nombre',
        'apellido_paterno',
        'apellido_materno',
        'correo_electronico',
    )
    readonly_fields = ['clave_de_registro', ]


class RegistroCongresoAdmin(admin.ModelAdmin):
    list_display = (
        'clave_de_registro',
        'nombre',
        'apellido_paterno',
        'apellido_materno',
        'correo_electronico',
        'escuela_de_procedencia',
        'es_alumno_ITA',
    )
    search_fields = (
        'clave_de_registro',
        'nombre',
        'apellido_paterno',
        'apellido_materno',
        'correo_electronico',
    )
    readonly_fields = ['clave_de_registro', ]


class RegistroMesasDeDebateAdmin(admin.ModelAdmin):
    list_display = (
        'clave_de_registro',
        'nombre',
        'apellido_paterno',
        'apellido_materno',
        'correo_electronico',
        'escuela_de_procedencia',
        'es_alumno_ITA',
    )
    search_fields = (
        'clave_de_registro',
        'nombre',
        'apellido_paterno',
        'apellido_materno',
        'correo_electronico',
    )
    readonly_fields = ['clave_de_registro', ]

admin.site.register(Curso, CursoAdmin)
admin.site.register(Conferencista, ConferencistaAdmin)

admin.site.register(RegistroCurso, RegistroCursoAdmin)
admin.site.register(RegistroCongreso, RegistroCongresoAdmin)
admin.site.register(RegistroMesasDeDebate, RegistroMesasDeDebateAdmin)
