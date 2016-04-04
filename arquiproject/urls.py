from blog.views import (
    AcreditacionView,
    DocentesView,
    HistoriaView,
    MisionVisionView,
    NoticiaView,
    NoticiasView,
    PerfilIngresoView
)

from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib import admin


urlpatterns = patterns(
    '',
    url(
        r'^admin/',
        include(admin.site.urls)
    ),
    # INDEX
    url(
        r'^$',
        'blog.views.index',
        name='index'
    ),
    # NOTICIAS
    url(
        r'^noticia/(?P<slug>[-\w]+)/$',
        NoticiaView.as_view(),
        name='noticia'
    ),
    # TODAS LAS NOTICIAS
    url(
        r'^noticias/$',
        NoticiasView.as_view(),
        name='noticias'
    ),
    # HISTORIA
    url(
        r'^historia/$',
        HistoriaView.as_view(),
        name='historia'
    ),
    # MISION-VISION
    url(
        r'^mision-vision/$',
        MisionVisionView.as_view(),
        name='mision_vision'
    ),
    # PERFIN DE INGRESO Y EGRESO
    url(
        r'^perfil-ingreso/$',
        PerfilIngresoView.as_view(),
        name='perfil_ingreso'
    ),
    # ACREDITACION
    url(
        r'^acreditacion/$',
        AcreditacionView.as_view(),
        name='acreditacion'
    ),
    # DOCENTES
    url(
        r'^docentes/$',
        DocentesView.as_view(),
        name='construccion'
    ),
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
    # CKEDITOR
    url(r'^ckeditor/', include('ckeditor.urls')),
)
handler404 = 'blog.views.e404'
