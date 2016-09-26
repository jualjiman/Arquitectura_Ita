# -*- coding: utf-8 -*-
from django import template
from django.forms.widgets import CheckboxInput

register = template.Library()


@register.filter(name='addclass')
def addclass(value, arg):
    if not isinstance(value.field.widget, CheckboxInput):
        return value.as_widget(attrs={'class': arg})
    return value

