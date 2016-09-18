# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Entrada, Semblanza, Slider


def index(request):
    sliders = Slider.objects.filter(
        activo=True
    )
    entradas = Entrada.objects.filter(
        activo=True
    )[:6]

    return render(
        request,
        "index.html",
        {
            "entradas": entradas,
            "slides": sliders,
        }
    )


class NoticiaView(DetailView):
    queryset = Entrada.objects.filter(activo=True)
    template_name = 'noticia.html'


class NoticiasView(ListView):
    queryset = Entrada.objects.filter(
        activo=True
    ).order_by(
        'titulo'
    )
    template_name = 'noticias.html'


class SemblanzasView(ListView):
    queryset = Semblanza.objects.filter(
        activo=True
    ).order_by(
        'nombre'
    )
    context_object_name = 'semblanzas'
    template_name = 'docentes.html'


class SemblanzaView(DetailView):
    queryset = Semblanza.objects.filter(
        activo=True
    )
    context_object_name = 'semblanza'
    template_name = 'docente.html'


def e404(request):
    return render(
        request,
        '404.html',
        {}
    )
