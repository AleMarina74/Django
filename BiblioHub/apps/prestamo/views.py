from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.utils.timezone import now
from .models import Prestamo
from .forms import PrestamoForm
import datetime

@login_required(login_url='ingresar')
def prestamoviews(request, id):
    prestamos = Prestamo.objects.filter(id=id)
    context = {
        "page_heading": "Prestamo",
        "prestamo": prestamos[0] if len(prestamos) else None,
        "USER": request.user
    }

    return render(request=request, template_name='prestamo.html', context=context)

@login_required(login_url='login')
def prestamosviews(request):
    paginator = Paginator(Prestamo.objects.all(), 10)
    page_number = request.GET.get("page")
    context = {
        "page_heading": "Prestamos",
        "prestamos": paginator.get_page(page_number),
        "field_keys": [field.attname for field in Prestamo._meta.get_fields()],
        "USER": request.user
    }
    return render(request=request, template_name='prestamos.html', context=context)

class PrestamosTemplateView(LoginRequiredMixin,TemplateView):
    template_name = 'prestamos.html'
    paginate_by = 10


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        prestamos = Prestamo.objects.filter(devolucion=False).order_by('cliente')
        paginator = Paginator(prestamos,self.paginate_by)
        page_number = self.request.GET.get("page") 
        context['prestamos']= paginator.get_page(page_number)
        context['USER'] = self.request.user
        context['page_heading'] = 'Prestamos'
        #context["field_keys"] = [field for field in Cliente._meta.get_fields()]
        fields = [
        {'name': 'libro', 'label': 'nombre', 'show': True},
        {'name': 'cliente', 'label': 'apellido', 'show': True},
        {'name': 'fecha_prestamo', 'label': 'dni', 'show': True},
        {'name': 'fecha_devolucion', 'label': 'domicilio', 'show': True},
        {'name': 'devolucion', 'label': 'Disponible', 'show': True},
  ]
        context['fields'] = fields
        return context

class PrestamoCreateView(LoginRequiredMixin,CreateView):
    model = Prestamo
    form_class = PrestamoForm
    template_name = 'crear_prestamo.html'
    success_url = reverse_lazy('prestamos')

    def get_initial(self):
        initial = super().get_initial()
        initial['fecha_prestamo'] = now().date()  # Obtiene la fecha actual sin hora
        return initial
    
    def form_valid(self, form):
        prestamo = form.save(commit=False)
        
        prestamo.devolucion = False

        fecha_prestamo = form.cleaned_data.get('fecha_prestamo')
        if fecha_prestamo:
            prestamo.fecha_prestamo = fecha_prestamo
        else:
            prestamo.fecha_prestamo = datetime.datetime.now()

        prestamo.save()

        libro = prestamo.libro
        cliente = prestamo.cliente
        libro.disponible = False
        cliente.disponible = False
        libro.save()
        cliente.save()

        return super().form_valid(form)
    
class DevolucionCreateView(LoginRequiredMixin, UpdateView):
    model = Prestamo
    fields = ['fecha_devolucion']
    template_name = 'crear_devolucion.html'
    success_url = '/prestamos/'  # URL a la que se redirige después de guardar la devolución

    def form_valid(self, form):
        prestamo = form.save(commit=False)
        prestamo.devolucion = True
        prestamo.save()

        libro = prestamo.libro
        cliente = prestamo.cliente
        libro.disponible = True
        cliente.disponible = True
        libro.save()
        cliente.save()

        return super().form_valid(form)

    def get_object(self, queryset=None):
        # Obtiene el objeto de Prestamo en función del parámetro de URL 'pk'
        return get_object_or_404(Prestamo, pk=self.kwargs['pk'])



class PrestamoCreate(LoginRequiredMixin,CreateView):
    model = Prestamo
    template_name = 'prestamo_form.html'
    fields = ['libro','cliente','fecha_prestamo','fecha_devolucion']
    success_url = reverse_lazy('prestamos')


class PrestamoDetail(LoginRequiredMixin,DetailView):
    model = Prestamo
    template_name = 'prestamo_detail.html'
    context_object_name = 'prestamo'


class PrestamoUpdate(LoginRequiredMixin,UpdateView):
    model = Prestamo
    template_name = 'prestamo_form.html'
    fields = ['libro','cliente', 'fecha_prestamo','fecha_devolucion']
    success_url = reverse_lazy('prestamos')


class PrestamoList(LoginRequiredMixin,ListView):
    model = Prestamo
    template_name = 'prestamo_list.html'
    context_object_name = 'prestamos'
