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


class NoticiasView(DetailView):
    model = Entrada


class TodasNView(ListView):
    model = Entrada


class HistoriaView(ListView):
    model = Entrada


class MisionVisionView(ListView):
    model = Entrada


class PerfilIngresoView(ListView):
    model = Entrada


class AcreditacionView(ListView):
    model = Entrada


class DocentesView(ListView):
    model = Entrada


def e404(request):
    return render(
        request,
        '404.html',
        {}
    )
