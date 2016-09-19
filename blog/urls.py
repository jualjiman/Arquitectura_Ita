# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from .views import (
    NoticiaView, NoticiasView,
    SemblanzaView, SemblanzasView
)


urlpatterns = patterns(
    '',
    url(
        r'^$',
        'blog.views.index',
        name='index'
    ),
    url(
        r'^noticia/(?P<slug>[-\w]+)/$',
        NoticiaView.as_view(),
        name='noticia'
    ),
    url(
        r'^noticias/$',
        NoticiasView.as_view(),
        name='noticias'
    ),
    url(
        r'^historia/$',
        TemplateView.as_view(
            template_name='historia.html'
        ),
        name='historia'
    ),
    url(
        r'^mision-vision/$',
        TemplateView.as_view(
            template_name='mision-vision.html'
        ),
        name='mision_vision'
    ),
    url(
        r'^perfil-ingreso/$',
        TemplateView.as_view(
            template_name='perfil-ingreso.html'
        ),
        name='perfil_ingreso'
    ),
    url(
        r'^acreditacion/$',
        TemplateView.as_view(
            template_name='acreditacion.html'
        ),
        name='acreditacion'
    ),
    url(
        r'^objetivo-general/$',
        TemplateView.as_view(
            template_name='objetivo-general.html'
        ),
        name='objetivo_general'
    ),
    url(
        r'^campo-de-trabajo/$',
        TemplateView.as_view(
            template_name='campo-de-trabajo.html'
        ),
        name='campo_de_trabajo'
    ),
    url(
        r'^docentes/$',
        SemblanzasView.as_view(),
        name='docentes'
    ),
    url(
        r'^docente/(?P<slug>[-\w]+)/$',
        SemblanzaView.as_view(),
        name='docente'
    ),
)
