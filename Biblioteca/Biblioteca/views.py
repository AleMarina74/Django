from django.shortcuts import render, redirect
from .forms import RegisterUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

ENCABEZADO = "Mesa de Entrada"

@login_required(login_url='ingresar')
def inicio(request):
    context = {
        "encabezado": ENCABEZADO,
        "USER": request.user 
    }
    return render(request=request, template_name='base.html', context=context)

def ingresar(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            messages.info(request, 'Usuario o password incorrecto.')
    context = {
        "encabezado": "Ingresar",
        "USER": request.user 
    }
    return render(request=request, template_name='ingresar.html', context=context)

def registrar(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Registro exitoso para ' + username)
            return redirect('ingresar')
    else:
        form = RegisterUser()
    context = {
        "form": form,
        "encabezado": "Registrar",
        "USER": request.user
    }
    return render(request=request, template_name='registrar.html', context=context)

@login_required(login_url='ingresar')
def cerrar(request):
    logout(request)
    return redirect('ingresar')