# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib import admin


urlpatterns = patterns(
    '',
    url(
        r'^admin/',
        include(admin.site.urls)
    ),
    url(
        r'',
        include('blog.urls', namespace='main')
    ),
    url(
        r'congreso/',
        include('congreso.urls', namespace='congreso')
    ),
    url(
        r'^ckeditor/',
        include('ckeditor.urls')
    ),

    # Static files routes, only used when in debugging mode.
    url(
        r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {
            'document_root': settings.STATIC_ROOT
        }
    ),
    url(
        r'^media/(?P<path>.*)$',
        'django.views.static.serve',
        {
            'document_root': settings.MEDIA_ROOT
        }
    ),
)

handler404 = 'blog.views.e404'
