
from email.policy import default
from random import choices, random
from turtle import position
from unicodedata import category
from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Category(models.Model):
    nom = models.CharField(max_length=50)
    image = models.ImageField(upload_to="imageCat", null=False, blank=True)
    slug = models.SlugField(null=True, blank=True)
    
    class Meta:
        verbose_name = ("Catégorie")
        verbose_name_plural = ("Catégories")
    
        
    def __str__(self):
        return self.nom
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)
        super().save(*args, **kwargs)        

class Niveau(models.Model):
    nom = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Niveaux')
    
    class Meta:
        verbose_name = ("Niveau")
        verbose_name_plural = ("Niveaux")
    
    
    def __str__(self):
        return self.nom
    


    



        
class Theme(models.Model):
    title = models.CharField(max_length=50)
    mini_description = models.TextField(verbose_name="Minie description", null=False)
    description = RichTextField()
    miniature = models.ImageField(upload_to="miniatures")
    slug = models.SlugField(null=True, blank=True)
    video = models.FileField(upload_to="videos", verbose_name="Vidéo")
    prix = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    document_pdf = models.FileField(verbose_name="Document PDF", null=True)
    categorie = models.ForeignKey(Category,on_delete=models.CASCADE)
    auteur = models.ForeignKey(User,on_delete=models.CASCADE)
    identifiant = models.CharField(null=True, max_length=100, blank=True)
    timing = models.PositiveIntegerField(null=True, verbose_name="Durée de la formation en heure")

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.identifiant = (uuid.uuid4())
        super().save(*args, **kwargs)
        
 

class Commentaire(models.Model):
    userame = models.CharField(max_length=50)
    message = RichTextField(null=False)
    date = models.DateTimeField(auto_now=True)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = ("Commentaire")
        verbose_name_plural = ("commentaires")

    def __str__(self):
        return self.userame



    

class profil(models.Model):
    choix = [
        ("Homme", "Homme"),
        ("Femme", "Femme"),
    ]
    
    choix_prof =  [
        ("Etudiant", "Etudiant"),
        ("Professionnel", "Professionnel"),
        ("Eleve", "Eleve"),
        ("Autodidacte", "Autodidacte"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    genre = models.CharField(max_length=80, choices=choix)

    image = models.ImageField(
        blank=True, upload_to="img", null= False, default="default.jpg")
    statut = models.CharField(max_length=80, choices=choix_prof)
    profession = models.CharField(max_length=50, null=False)

    
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username
    

class historique(models.Model):

    user = models.ForeignKey(User, verbose_name=("Utilisateur"), on_delete=models.CASCADE)
    theme_id = models.CharField(max_length=1000, null=True)
    identifiant = models.CharField(max_length=1000)
    prix = models.CharField(max_length=1000)
    
    date = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = ("Order par theme")
        verbose_name_plural = ("Order par theme")

    def __str__(self):
        return f'{self.user.username} a prix le theme " {self.theme_id} "'
    

   
    
    

class etudiant(profil):
    bio = RichTextField(null = False)
    def __str__(self):
        return self.user.username


class professeur(profil):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, null=False)
    bio = models.TextField(null = False)
    def __str__(self):
        return self.user.username
    

class email(models.Model):
    email = models.EmailField(max_length=254)
    date = models.DateField(auto_now_add=True)
    

    class Meta:
        verbose_name = ("Abonnée")
        verbose_name_plural = ("Abonnées")

    def __str__(self):
        return self.email



# ----------------------------devenir prof ----------------------
class demande(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    nom = models.CharField( max_length=50)
    prenom = models.CharField(verbose_name='Prénom ', max_length=50)
    etude = models.CharField(verbose_name="Niveau d'étude", max_length=50)
    telephone = models.CharField(verbose_name="Numéro de telephone", max_length=200)
    motivation = models.TextField(verbose_name="Vos motivations", max_length=200)
    Date = models.DateField(auto_now_add=True)
    
    

    class Meta:
        verbose_name = ("Demande")
        verbose_name_plural = ("Demandes")

    def __str__(self):
        return self.user.username


    
    
    

