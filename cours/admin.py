from genericpath import samefile
from django.contrib import admin
from .models import *
from django.contrib.admin import AdminSite



# Register your models here.

    
admin.site.site_header = "Le Pro'Gram 🤖"

admin.site.register(Niveau)
admin.site.register(Category)
admin.site.register(Theme)
admin.site.register(Commentaire)
admin.site.register(etudiant)
admin.site.register(professeur)
admin.site.register(historique)
admin.site.register(email)
admin.site.register(demande)
