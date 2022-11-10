from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ("__all__")
        exclude = ('theme','date','auteur')
        

class ConnexionForm(forms.Form):
    username = forms.CharField(label='Nom d\'utilisation', max_length=60)
    password = forms.CharField(
        label="Mot de passe", widget=forms.PasswordInput)

class ProfilForm(forms.ModelForm):
    class Meta:
        model = etudiant
        fields = ('__all__')
        exclude = ('user',)
        


        
class add_themeForm(forms.ModelForm):
    class Meta:
        model = Theme
        field = ('__all__')
        exclude = ('auteur','slug', 'identifiant')

class emailForm(forms.ModelForm):
    class Meta:
        model = email
        field = ('email',)
        exclude = ('date',)

class demandeForm(forms.ModelForm):
    class Meta:
        model = demande
        field = ('__all__')
        exclude = ("user",)
        

    

