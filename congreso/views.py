# -*- coding: utf-8 -*-
from django.views.generic import DetailView, ListView

from .models import Conferencista, Curso


class HomeView(ListView):
    queryset = Conferencista.objects.filter(
        activo=True
    ).order_by(
        'nombre'
    )
    context_object_name = 'conferencistas'
    template_name = 'congreso/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['cursos'] = Curso.objects.filter(
            activo=True
        ).order_by(
            'nombre'
        )[:6]
        return context


class ConferencistasView(ListView):
    queryset = Conferencista.objects.filter(
        activo=True
    ).order_by(
        'nombre'
    )
    context_object_name = 'conferencistas'
    template_name = 'congreso/conferencistas.html'


class ConferencistaView(DetailView):
    queryset = Conferencista.objects.filter(
        activo=True
    )
    context_object_name = 'conferencista'
    template_name = 'congreso/conferencista.html'


class CursosView(ListView):
    queryset = Curso.objects.filter(
        activo=True
    ).order_by(
        'nombre'
    )
    context_object_name = 'cursos'
    template_name = 'congreso/cursos.html'


class CursoView(DetailView):
    queryset = Curso.objects.filter(
        activo=True
    )
    context_object_name = 'curso'
    template_name = 'congreso/curso.html'
