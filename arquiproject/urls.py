from django.conf.urls import patterns, include, url
from django.contrib import admin
#from django.views.generic import TemplateView
from django.views.generic import ListView,DetailView
from blog.views import NoticiasView,TodasNView,HistoriaView,MisionVisionView,PerfilIngresoView,AcreditacionView
from django.conf import settings



urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'arquiproject.views.home', name='home'),
   # url(r'^$', include('blog.urls')),

    #url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
   # INDEX
   url(r'^$', 'blog.views.index', name='index'),
   #NOTICIAS
   url(r'^noticias/(?P<slug>[-\w]+)/$', (NoticiasView.as_view(template_name = "noticias.html"))),
   #TODAS LAS NOTICIAS
   url(r'^noticias-todas/$', (TodasNView.as_view(template_name = "noticias-todas.html"))),
   #HISTORIA
   url(r'^historia/$', (HistoriaView.as_view(template_name = "historia.html"))),
   #MISION-VISION
   url(r'^mision-vision/$', (MisionVisionView.as_view(template_name = "mision-vision.html"))),
   #PERFIN DE INGRESO Y EGRESO
   url(r'^perfil-ingreso/$', (PerfilIngresoView.as_view(template_name = "perfil-ingreso.html"))),
   #ACREDITACION
    url(r'^acreditacion/$', (AcreditacionView.as_view(template_name = "acreditacion.html"))),

   
   url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT} ),
   #CKEDITOR
	(r'^ckeditor/', include('ckeditor.urls')),


	
	


    #url(r'^noticias/(\d+)/$', 'blog.views.noticias', name='noticias'),


)

