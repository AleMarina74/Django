from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Autor
# Create your views here.

class AutorList(ListView,LoginRequiredMixin):
    model = Autor
    template_name = 'autor_list.html'
    context_object_name = 'autor'

class AutorCreate(CreateView,LoginRequiredMixin):
    model = Autor
    template_name = 'autor_form.html'
    fields = ['nombre']
    success_url = reverse_lazy('createbook')


class AutorDetail(DetailView,LoginRequiredMixin):
    model = Autor
    template_name = 'autor_detail.html'
    context_object_name = 'autor'

class AutorUpdate(UpdateView,LoginRequiredMixin):
    model = Autor
    template_name = 'autor_form.html'
    fields = ['nombre']
    success_url = reverse_lazy('autor')