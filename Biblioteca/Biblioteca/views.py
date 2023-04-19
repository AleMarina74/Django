from django.shortcuts import render
ENCABEZADO = "Mesa de Entrada"
# Create your views here.
def home(request):
    return render(request=request, template_name='base.html', context={"encabezado":ENCABEZADO})