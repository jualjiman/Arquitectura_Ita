from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib import admin

from blog.views import *


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    # INDEX
    url(r'^$', 'blog.views.index', name='index'),
    # NOTICIAS
    url(r'^noticias/(?P<slug>[-\w]+)/$', (NoticiasView.as_view(template_name="noticias.html"))),
    # TODAS LAS NOTICIAS
    url(r'^noticias-todas/$', (TodasNView.as_view(template_name="noticias-todas.html"))),
    # HISTORIA
    url(r'^historia/$', (HistoriaView.as_view(template_name="historia.html"))),
    # MISION-VISION
    url(r'^mision-vision/$', (MisionVisionView.as_view(template_name="mision-vision.html"))),
    # PERFIN DE INGRESO Y EGRESO
    url(r'^perfil-ingreso/$', (PerfilIngresoView.as_view(template_name="perfil-ingreso.html"))),
    # ACREDITACION
    url(r'^acreditacion/$', (AcreditacionView.as_view(template_name="acreditacion.html"))),
    # DOCENTES
    url(r'^docentes/$', (DocentesView.as_view(template_name="construccion.html"))),
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
