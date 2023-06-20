from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Genero
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy



class GeneroList(ListView,LoginRequiredMixin):
    model = Genero
    template_name = 'genero_list.html'
    context_object_name = 'genero'

class GeneroCreate(CreateView,LoginRequiredMixin):
    model = Genero
    template_name = 'genero_form.html'
    fields = ['nombre']
    success_url = reverse_lazy('createbook')


class GeneroDetail(DetailView,LoginRequiredMixin):
    model = Genero
    template_name = 'genero_detail.html'
    context_object_name = 'genero'

class GeneroUpdate(UpdateView,LoginRequiredMixin):
    model = Genero
    template_name = 'genero_form.html'
    fields = ['nombre']
    success_url = reverse_lazy('genero')