from django.db import models

class Identifiant(models.Model):
    name = models.fields.CharField(max_length = 100)
    age = models.fields.IntegerField()


# Create your models here.
