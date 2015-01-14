from django.views.generic import ListView,DetailView
from .models import Entrada,Slider
from .models import *


# Create your views here.
#def index(request):
	
	#return render_to_response('index.html')

class IndexView(ListView):
	
	template_name = "index.html"
	model = Entrada

	
	

class TodasNView(ListView):
	template_name = "noticias-todas.html"
	model  = Entrada
	


class NoticiasView(DetailView):
	template_name = "noticias.html"
	model = Entrada
	