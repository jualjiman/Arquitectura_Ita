# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm

from .models import RegistroCongreso, RegistroCurso, RegistroMesasDeDebate


class RegistroCursoForm(ModelForm):
    class Meta:
        model = RegistroCurso
        fields = [
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'numero_control',
            'correo_electronico',
            'escuela_de_procedencia',
            'folio_recibo_oficial',
            'estado_municipio',
            'curso',
        ]

    def clean(self):
        cleaned_data = super(RegistroCursoForm, self).clean()
        #
        # Checking if there is available spaces to being registered
        # to the course.
        #
        course_register_limit = 30
        if 'curso' in cleaned_data:
            course = cleaned_data['curso']
            course_registers_count = RegistroCurso.objects.filter(
                curso=course
            ).count()

            if not course_registers_count < course_register_limit:
                raise forms.ValidationError(
                    'Se ha alcanzado el cupo máximo de '
                    '<strong>{0} espacios</strong> para el curso '
                    '<strong>"{1}"</strong>, por favor intenta con otro '
                    'curso de tu interés.'.format(
                        course_register_limit,
                        course.nombre.encode('utf-8')
                    )
                )

        return cleaned_data


class RegistroCongresoForm(ModelForm):
    class Meta:
        model = RegistroCongreso
        fields = [
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'numero_control',
            'correo_electronico',
            'escuela_de_procedencia',
            'folio_recibo_oficial',
            'estado_municipio',
            'tipo_de_inscripcion',
        ]

    def clean(self):
        cleaned_data = super(RegistroCongresoForm, self).clean()
        #
        # Checking if there is available spaces to being registered
        # to the congress.
        #
        congress_register_limit = 900
        congress_registers_count = RegistroCongreso.objects.all().count()

        if not congress_registers_count < congress_register_limit:
            raise forms.ValidationError(
                'Se ha alcanzado el cupo máximo de '
                '<strong>{0} espacios</strong> para el congreso, no fue '
                'posible completar el registro.'.format(
                    congress_register_limit
                )
            )

        return cleaned_data


class RegistroMesasDeDebateForm(ModelForm):
    class Meta:
        model = RegistroMesasDeDebate
        fields = [
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'correo_electronico',
            'escuela_de_procedencia',
            'es_alumno_ITA',
            'folio_recibo_oficial',
            'estado_municipio',
            'archivo_sintesis',
        ]

    def clean(self):
        cleaned_data = super(RegistroMesasDeDebateForm, self).clean()
        #
        # Checking if there is available spaces to being registered
        # to the discussion tables.
        #
        discussions_register_limit = 100
        discussions_registers_count = (
            RegistroMesasDeDebate.objects.all().count()
        )

        if not discussions_registers_count < discussions_register_limit:
            raise forms.ValidationError(
                'Se ha alcanzado el cupo máximo de '
                '<strong>{0} espacios</strong> para las mesas de debate,'
                ' no fue posible completar el registro.'.format(
                    discussions_register_limit
                )
            )

        return cleaned_data
