from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy

from .models import Libro

@login_required(login_url='ingresar')
def books(request):
    paginator = Paginator(Libro.objects.all(), 10)
    page_number = request.GET.get("page")
    context = {
        "page_heading": "Libros",
        "books": paginator.get_page(page_number),
        "field_keys": [field.attname for field in Libro._meta.get_fields()],
        "USER": request.user
    }
    return render(request=request, template_name='books.html', context=context)

@login_required(login_url='ingresar')
def book(request, id):
    return BookTemplateView.as_view()(request, id=id)


class BooksTemplateView(TemplateView):
    template_name = 'books.html'
    paginate_by = 10


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = Libro.objects.all()
        paginator = Paginator(books,self.paginate_by)
        page_number = self.request.GET.get("page") 
        context['books']= paginator.get_page(page_number)
        context['USER'] = self.request.user
        context['page_heading'] = 'Libros'
        context["field_keys"] = [field.verbose_name for field in Libro._meta.get_fields()]

        return context

    

class BookTemplateView(TemplateView):
    template_name = 'book.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = get_object_or_404(Libro, id=self.kwargs['id'])
        context["page_heading"] = "Libro"
        context["book"] = book
        context["USER"] = self.request.user
        context["field_keys"] = [field.verbose_name for field in Libro._meta.get_fields()]
        return context

class BookList(ListView):
    model = Libro
    template_name = 'book_list.html'
    context_object_name = 'libro'


class BookCreate(CreateView):
    model = Libro
    template_name = 'book_form.html'
    fields = ['titulo', 'autor', 'genero', 'isbn','borrado','disponible']
    success_url = reverse_lazy('books')

class BookDetail(DetailView):
    model = Libro
    template_name = 'book_detail.html'
    context_object_name = 'book'

class BookUpdate(UpdateView):
    model = Libro
    template_name = 'book_form.html'
    fields = ['titulo', 'autor', 'genero', 'isbn','borrado','disponible']
    success_url = reverse_lazy('books')

class BookDelete(DeleteView):
    model = Libro
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('books')


       