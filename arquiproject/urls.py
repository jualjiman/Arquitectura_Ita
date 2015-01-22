from django.conf.urls import patterns, include, url
from django.contrib import admin
#from django.views.generic import TemplateView
from django.views.generic import ListView
from blog.views import NoticiasView,TodasNView
from django.conf import settings



urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'arquiproject.views.home', name='home'),
   # url(r'^$', include('blog.urls')),

    #url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
   # url(r'^$', "blog.views.index", name='index'),
   url(r'^$', 'blog.views.index', name='index'),
   url(r'^noticias/(?P<slug>[-\w]+)/$', (NoticiasView.as_view(template_name = "noticias.html"))),
   url(r'^noticias-todas/$', (TodasNView.as_view(template_name = "noticias-todas.html"))),
   url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT} ),
   #url(r'^markdown/', include('django_markdown.urls')),
	(r'^ckeditor/', include('ckeditor.urls')),


	
	


    #url(r'^noticias/(\d+)/$', 'blog.views.noticias', name='noticias'),


)

