from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "index.html")

def inquilinos(request):
    return render(request, "inquilinos.html")

def unidades(request):
    return render(request, "unidades.html")

