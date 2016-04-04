from blog.views import (
    DocentesView,
    NoticiaView,
    NoticiasView,
)

from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = patterns(
    '',
    url(
        r'^admin/',
        include(admin.site.urls)
    ),
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
        DocentesView.as_view(),
        name='construccion'
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
