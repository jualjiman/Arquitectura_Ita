from django.views.generic import ListView,DetailView
from .models import Entrada,Slider
from .models import *
from django.db.models import Q
from django.shortcuts import render,get_object_or_404


# Create your views here.
#def index(request):
	
	#return render_to_response('index.html')


class IndexView(ListView):
	
	entradas = Entrada.objects.all()[:3]
	template_name = "index.html"
	
	model = Entrada
	
	

	
	

class TodasNView(ListView):
	template_name = "noticias-todas.html"
	model  = Entrada
	


class NoticiasView(DetailView):
	template_name = "noticias.html"
	model = Entrada
	