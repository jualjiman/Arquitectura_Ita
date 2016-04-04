from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Entrada, Slider


def index(request):
    sliders = Slider.objects.filter(activo=True)
    entradas = Entrada.objects.all()[:6]

    return render(
        request,
        "index.html",
        {
            "entradas": entradas,
            "sliders": sliders,
        }
    )


class NoticiaView(DetailView):
    model = Entrada
    template_name = 'noticia.html'


class NoticiasView(ListView):
    model = Entrada
    template_name = 'noticias.html'


class HistoriaView(ListView):
    model = Entrada
    template_name = 'historia.html'


class MisionVisionView(ListView):
    model = Entrada
    template_name = "mision-vision.html"


class PerfilIngresoView(ListView):
    model = Entrada
    template_name = "perfil-ingreso.html"


class AcreditacionView(ListView):
    model = Entrada
    template_name = "acreditacion.html"


class DocentesView(ListView):
    model = Entrada
    template_name = "construccion.html"


def e404(request):
    return render(
        request,
        '404.html',
        {}
    )
