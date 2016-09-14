from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Entrada, Semblanza, Slider


def index(request):
    sliders = Slider.objects.filter(activo=True)
    entradas = Entrada.objects.all()[:6]

    return render(
        request,
        "index.html",
        {
            "entradas": entradas,
            "slides": sliders,
        }
    )


class NoticiaView(DetailView):
    model = Entrada
    template_name = 'noticia.html'


class NoticiasView(ListView):
    model = Entrada
    template_name = 'noticias.html'


class SemblanzasView(ListView):
    model = Semblanza
    context_object_name = 'semblanzas'
    template_name = 'docentes.html'


class SemblanzaView(DetailView):
    queryset = Semblanza.objects.filter(activo=True).order_by('nombre')
    context_object_name = 'semblanza'
    template_name = 'docente.html'


def e404(request):
    return render(
        request,
        '404.html',
        {}
    )
