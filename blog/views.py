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


def e404(request):
    return render(
        request,
        '404.html',
        {}
    )
