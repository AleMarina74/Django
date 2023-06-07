from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Cliente
from django.views.generic.base import TemplateView
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

@method_decorator(login_required, name='dispatch')
class ClientesTemplateView(TemplateView):
    template_name = 'clients.html'
    paginate_by = 10


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        clientes = Cliente.objects.all()
        paginator = Paginator(clientes,self.paginate_by)
        page_number = self.request.GET.get("page") 
        context['clients']= paginator.get_page(page_number)
        context['USER'] = self.request.user
        context['page_heading'] = 'Clientes'
        context["field_keys"] = [field.verbose_name for field in Cliente._meta.get_fields()]

        return context

@method_decorator(login_required, name='dispatch')
class ClienteList(ListView):
    model = Cliente
    template_name = 'cliente.html'
    context_object_name = 'clientes'


class ClienteCreate(LoginRequiredMixin,CreateView):
    model = Cliente
    template_name = 'client_form.html'
    fields = ['nombre', 'apellido', 'dni', 'fecha_nacimiento','email','domicilio']
    success_url = reverse_lazy('clientes')

@method_decorator(login_required, name='dispatch')
class ClienteDetail(DetailView):
    model = Cliente
    template_name = 'client_detail.html'
    context_object_name = 'clientes'

@method_decorator(login_required, name='dispatch')
class ClienteUpdate(UpdateView):
    model = Cliente
    template_name = 'client_form.html'
    fields = ['nombre', 'apellido', 'dni', 'fecha_nacimiento','email','domicilio']
    success_url = reverse_lazy('clients')

@method_decorator(login_required, name='dispatch')
class ClienteDelete(DeleteView):
    model = Cliente
    template_name = 'client_confirm_delete.html'
    success_url = reverse_lazy('clients')