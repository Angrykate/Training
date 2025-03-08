from django.contrib import admin
from Biblio.models import Categorie, Livre

# Register your models here.
class LivreAdmin(admin.ModelAdmin):
    list_display = ('titre','categorie')

admin.site.register(Categorie)
admin.site.register(Livre,LivreAdmin)
