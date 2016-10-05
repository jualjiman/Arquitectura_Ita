# -*- coding: utf-8 -*-
import random
from hashlib import md5

from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView

from .forms import (
    RegistroCongresoForm, RegistroCursoForm,
    RegistroMesasDeDebateForm
)
from .models import (
    Conferencista, Curso,
    RegistroCongreso, RegistroCurso, RegistroMesasDeDebate
)


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
    template_name = 'congreso/conferencistas/list.html'


class ConferencistaView(DetailView):
    queryset = Conferencista.objects.filter(
        activo=True
    )
    context_object_name = 'conferencista'
    template_name = 'congreso/conferencistas/detail.html'


class CursosView(ListView):
    queryset = Curso.objects.filter(
        activo=True
    ).order_by(
        'nombre'
    )
    context_object_name = 'cursos'
    template_name = 'congreso/cursos/list.html'

    def get_context_data(self, **kwargs):
        context = super(CursosView, self).get_context_data(**kwargs)
        context['form'] = RegistroCursoForm()
        return context


class CursoView(DetailView):
    queryset = Curso.objects.filter(
        activo=True
    )
    context_object_name = 'curso'
    template_name = 'congreso/cursos/detail.html'


class BaseRegisterCreateView(SuccessMessageMixin, CreateView):

    def generate_register_key(self, instance):
        unique_data = "{0}{1}{2}{3}{4}{5}".format(
            instance.nombre,
            instance.apellido_paterno,
            instance.apellido_materno,
            instance.correo_electronico,
            instance.escuela_de_procedencia,
            random.randint(0, 10000000)
        )
        dirty_key = md5(unique_data).hexdigest()
        return (dirty_key[:8]).upper()

    def form_valid(self, form):
        self.register_key = self.generate_register_key(form.instance)
        form.instance.clave_de_registro = self.register_key
        return super(BaseRegisterCreateView, self).form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.dirty_success_message.format(
            cleaned_data['nombre'].encode('utf-8'),
            self.register_key
        )


class RegistroCursoCreateView(BaseRegisterCreateView):
    model = RegistroCurso
    form_class = RegistroCursoForm
    success_url = reverse_lazy('congreso:cursos')
    template_name = "congreso/cursos/create.html"
    dirty_success_message = (
        'Felicidades <strong>{0}</strong>! has sido registrado '
        'exitosamente al curso "<strong>{1}</strong>". '
        'Tu clave de registro es: <strong>{2}</strong>'
    )

    def get_success_message(self, cleaned_data):
        return self.dirty_success_message.format(
            cleaned_data['nombre'].encode('utf-8'),
            cleaned_data['curso'].nombre.encode('utf-8'),
            self.register_key
        )


class RegistroCongresoCreateView(BaseRegisterCreateView):
    model = RegistroCongreso
    form_class = RegistroCongresoForm
    success_url = reverse_lazy('congreso:home')
    template_name = "congreso/congreso/create.html"
    dirty_success_message = (
        'Felicidades <strong>{0}</strong>! has sido registrado '
        'exitosamente al <strong>Congreso</strong>. '
        'Tu clave de registro es: <strong>{1}</strong>'
    )


class RegistroMesasDeDebateCreateView(BaseRegisterCreateView):
    model = RegistroMesasDeDebate
    form_class = RegistroMesasDeDebateForm
    success_url = reverse_lazy('congreso:home')
    template_name = "congreso/mesasdebate/create.html"
    dirty_success_message = (
        'Felicidades <strong>{0}</strong>! has sido registrado '
        'exitosamente a las <strong>Mesas de debate</strong>. '
        'Tu clave de registro es: <strong>{1}</strong>'
    )
