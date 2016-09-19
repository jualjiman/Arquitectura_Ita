# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import (
    ConferencistaView, ConferencistasView
)


urlpatterns = patterns(
    '',
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
)
