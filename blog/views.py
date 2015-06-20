from django.views.generic import ListView,DetailView
from .models import Entrada
from .models import *
from django.http import Http404
from django.db.models import Q
from django.shortcuts import render,get_object_or_404


# Create your views here.
#def index(request):
	
	#return render_to_response('index.html')


def index(request):
	
	sliders = Slider.objects.filter(activo = True)
	entradas = Entrada.objects.all()[:6]
	
	

	return render(
					request,
					"index.html",
					{
					"entradas":entradas,
					"sliders":sliders,
					
					})
class NoticiasView(DetailView):
	model = Entrada


class TodasNView(ListView):
	model  = Entrada


class HistoriaView(ListView):
	model = Entrada

class MisionVisionView(ListView):
	model=Entrada

class PerfilIngresoView(ListView):
	model = Entrada

class AcreditacionView(ListView):
	model=Entrada

class DocentesView(ListView):
	model = Entrada


def e404(request):
	return render(request,
		'404.html',
		{}
		)



	