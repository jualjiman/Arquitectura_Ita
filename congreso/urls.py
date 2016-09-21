# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from .views import (
    ConferencistaView, ConferencistasView,
    CursoView, CursosView, HomeView
)


urlpatterns = patterns(
    '',
    url(
        r'^home/$',
        HomeView.as_view(),
        name='home'
    ),
    url(
        r'^conferencistas/$',
        ConferencistasView.as_view(),
        name='conferencistas'
    ),
    url(
        r'^conferencistas/(?P<slug>[-\w]+)/$',
        ConferencistaView.as_view(),
        name='conferencista'
    ),
    url(
        r'^cursos/$',
        CursosView.as_view(),
        name='cursos'
    ),
    url(
        r'^cursos/(?P<slug>[-\w]+)/$',
        CursoView.as_view(),
        name='curso'
    ),
    url(
        r'^convocatoria/$',
        TemplateView.as_view(
            template_name='congreso/convocatoria.html'
        ),
        name='convocatoria'
    ),
)
