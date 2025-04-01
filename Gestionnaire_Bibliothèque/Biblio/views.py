from django.shortcuts import render
from django.http import HttpResponse
from Biblio.models import Livre

# Create your views here.
def Affichage_livre(request):
    livres = Livre.objects.all()
    return render(request,"Biblio/liste_livres.html",context = {"livres":livres})

def Affichage_details_liste(request,id):
    livres = Livre.objects.get(id=id)
    return render(request,"Biblio/details_livre.html",context = {"livres":livres})