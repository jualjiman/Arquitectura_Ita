# -*- coding: utf-8 -*-
from django.contrib import admin

from reports.actions import export_as_csv

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


class RegistroModelAdmin(admin.ModelAdmin):
    #
    # Campos base.
    #
    list_display_fields = [
        'clave_de_registro',
        'nombre_completo',
        'correo_electronico',
        'escuela_de_procedencia',
        'es_alumno_ITA',
    ]
    #
    # Campos extra, en caso de ser necesario.
    #
    list_display_extra_fields = []

    search_fields = [
        'clave_de_registro',
        'nombre',
        'apellido_paterno',
        'apellido_materno',
        'correo_electronico',
    ]
    readonly_fields = ['clave_de_registro', ]

    #
    # Configuraciones de reporte.
    #
    actions = [export_as_csv, ]
    #
    # Campos base para el reporte.
    #
    report_fields = [
        'clave_de_registro',
        'nombre_completo',
        'correo_electronico',
        'escuela_de_procedencia',
        'es_alumno_ITA',
        'folio_recibo_oficial',
        'estado_municipio',
        'es_valido',
    ]
    #
    # Campos extra, en caso de ser necesarios.
    #
    report_extra_fields = []
    #
    # Nombres para campos, deben seguir el mismo orden que la lista retornada,
    # por la funcion "get_report_fields".
    #
    report_field_names = [
        'Clave de registro',
        'Nombre completo',
        'Correo_electronico',
        'Escuela_de_procedencia',
        'Es alumno ITA',
        'Folio recibo oficial',
        'Estado municipio',
        'Es valido',
    ]
    report_field_extra_names = []
    #
    # Nombre dado al reporte.
    #
    report_name = ''

    @property
    def get_report_fields(self):
        return self.report_fields + self.report_extra_fields

    @property
    def get_report_name(self):
        return self.report_name

    @property
    def get_report_field_names(self):
        return self.report_field_names + self.report_field_extra_names

    def get_list_display(self, request):
        super(RegistroModelAdmin, self).get_list_display(request)
        return self.list_display_fields + self.list_display_extra_fields


class RegistroCursoAdmin(RegistroModelAdmin):
    list_display_extra_fields = [
        'curso',
    ]

    #
    # Configuracion de reporte.
    #
    report_name = 'registro_curso'
    report_extra_fields = ['curso', ]
    report_field_extra_names = ['Curso', ]

    list_filter = ['curso', ]


class RegistroCongresoAdmin(RegistroModelAdmin):
    list_display_extra_fields = [
        'tipo_de_inscripcion',
    ]

    #
    # Configuracion de reporte.
    #
    report_name = 'registro_congreso'
    report_extra_fields = ['tipo_de_inscripcion', ]
    report_field_extra_names = ['Tipo de inscripcion', ]
    list_filter = ['tipo_de_inscripcion', ]


class RegistroMesasDeDebateAdmin(RegistroModelAdmin):
    #
    # Configuracion de reporte.
    #
    report_name = 'registro_mesas_de_debate'


admin.site.register(Curso, CursoAdmin)
admin.site.register(Conferencista, ConferencistaAdmin)
admin.site.register(RegistroCurso, RegistroCursoAdmin)
admin.site.register(RegistroCongreso, RegistroCongresoAdmin)
admin.site.register(RegistroMesasDeDebate, RegistroMesasDeDebateAdmin)
