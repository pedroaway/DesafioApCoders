from django.shortcuts import render
from app.forms import PessoasForm, UnidadesForm


def home(request):
    return render(request, "index.html")

def inquilinos(request):
    return render(request, "inquilinos.html")

def unidades(request):
    return render(request, "unidades.html")

def inqForm(request):
    data = { }
    data['inqForm'] = PessoasForm()
    return render(request, "inqForm.html", data)

def uniForm(request):
    data = { }
    data['uniForm'] = UnidadesForm()
    return render(request, "uniForm.html", data)


