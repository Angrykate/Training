from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,"appli1/index.html",context = {})

def Acceuil(request):
    return render(request, "appli1/index2.html",context = {})

# Create your views here.
