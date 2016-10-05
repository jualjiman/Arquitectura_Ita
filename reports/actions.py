# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.utils import timezone

import unicodecsv as csv


def export_as_csv(model_admin, request, queryset):
    """
    function that dynamically creates CSV.
    """
    now = timezone.localtime(timezone.now()).strftime('%d-%m-%Y %H:%M')

    fields = model_admin.get_report_fields
    field_names = model_admin.get_report_field_names
    file_name = model_admin.get_report_name

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=%s.csv' % (
        file_name + '_' + now
    )

    writer = csv.writer(response)
    writer.writerow(field_names)

    TIPOS_INSCRIPCION = {
        'esita': u'Estudiantes ITA ($500.00)',
        'eotra': u'Estudiantes de otra institución ($600.00)',
        'egres': u'Egresados ITA ($700.00)',
        'profe': u'Profesionistas ($1,000.00)',
    }

    for item in queryset:
        row = []
        for field in fields:
            attr = getattr(item, field)

            if field == 'tipo_de_inscripcion':
                attr = TIPOS_INSCRIPCION[attr]

            elif type(attr) == bool:
                if attr:
                    attr = u'Si'
                else:
                    attr = u'No'

            row.append(attr)

        writer.writerow(row)

    return response

export_as_csv.short_description = "Exportar a CSV"
