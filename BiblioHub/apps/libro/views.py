from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Libro

@login_required(login_url='login')
def books(request):
    paginator = Paginator(Libro.objects.all(), 10)
    page_number = request.GET.get("page")
    context = {
        "page_heading": "Libros",
        "books": paginator.get_page(page_number),
        "field_keys": [field for field in Libro._meta.get_fields()],
        "USER": request.user
    }
    return render(request=request, template_name='books.html', context=context)

@login_required(login_url='ingresar')
def book(request, id):
    return BookTemplateView.as_view()(request, id=id)


class BooksTemplateView(TemplateView,LoginRequiredMixin):
    template_name = 'books.html'
    paginate_by = 10


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = Libro.objects.filter(borrado=False).order_by('titulo')
        paginator = Paginator(books,self.paginate_by)
        page_number = self.request.GET.get("page") 
        context['books']= paginator.get_page(page_number)
        context['USER'] = self.request.user
        context['page_heading'] = 'Libros'
       # context["field_keys"] = [field for field in Libro._meta.get_fields()]
        fields = [
        {'name': 'titulo', 'label': 'Título', 'show': True},
        {'name': 'autor', 'label': 'Autor', 'show': False},
        {'name': 'genero', 'label': 'Género', 'show': False},
        {'name': 'isbn', 'label': 'ISBN', 'show': True},
        {'name': 'disponible', 'label': 'Disponible', 'show': True},
    ]

        context['fields'] = fields
        return context

    

class BookTemplateView(TemplateView,LoginRequiredMixin):
    template_name = 'book.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = get_object_or_404(Libro, id=self.kwargs['id'])
        context["page_heading"] = "Libro"
        context["book"] = book
        context["USER"] = self.request.user
        context["field_keys"] = [field for field in Libro._meta.get_fields()]
        return context


class BookList(ListView,LoginRequiredMixin):
    model = Libro
    template_name = 'book_list.html'
    context_object_name = 'libro'


class BookCreate(CreateView,LoginRequiredMixin):
    model = Libro
    template_name = 'book_form.html'
    fields = ['titulo', 'autor', 'genero', 'isbn','borrado','disponible']
    success_url = reverse_lazy('books')

    def form_valid(self, form):
        form.instance.titulo = form.cleaned_data['titulo'].upper()

        isbn = form.cleaned_data['isbn']
        libro_existente = Libro.objects.filter(isbn=isbn).first()
        
        if libro_existente:
            form.add_error('isbn', f'El libro con ISBN {isbn} ya existe. Datos del libro: {libro_existente.titulo}, {libro_existente.autor}')
            return self.form_invalid(form)
        
        return super().form_valid(form)


class BookDetail(DetailView,LoginRequiredMixin):
    model = Libro
    template_name = 'book_detail.html'
    context_object_name = 'book'

class BookUpdate(UpdateView,LoginRequiredMixin):
    model = Libro
    template_name = 'book_form.html'
    fields = ['titulo', 'autor', 'genero', 'isbn','borrado','disponible']
    success_url = reverse_lazy('books')

    def form_valid(self, form):
        form.instance.titulo = form.cleaned_data['titulo'].upper()
 
        return super().form_valid(form)

class BookDelete(DeleteView,LoginRequiredMixin):
    model = Libro
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('books')


       