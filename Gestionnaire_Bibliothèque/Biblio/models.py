from django.db import models


# Create your models here.
class Categorie(models.Model):
    def __str__(self):
        return f'{self.nom}'
    
    nom = models.fields.CharField(max_length=50)


class Livre(models.Model):
    def __str__(self):
        return f'{self.titre}'
    
    titre = models.fields.CharField(max_length = 100)
    auteur = models.fields.CharField(max_length = 50)
    date_publication = models.fields.DateField(blank = True,null = True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    disponible = models.fields.BooleanField(default = True)
    description = models.fields.TextField(blank = True)
