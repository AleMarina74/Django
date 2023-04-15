from django.shortcuts import render
ENCABEZADO = "Clientes"
# Create your views here.
def clientes(request):
    return render(request=request, template_name='lista.html', context={"encabezado":ENCABEZADO})
