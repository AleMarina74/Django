from django.shortcuts import render
ENCABEZADO = "Libros"
# Create your views here.
def libros(request):
    return render(request=request, template_name='lista.html', context={"encabezado":ENCABEZADO})
