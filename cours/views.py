from multiprocessing import context
from threading import local
from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeDoneView, PasswordChangeView
from django.urls import reverse
from .forms import *
from django.db.models import Q


# Create your views here.

# class home(ListView):
#     model = Lesson
#     context_object_name = 'Lessons'
#     template_name = "cours/test/home.html"


# class home(ListView):
#     model = Theme
#     # ordering = "-date"
#     context_object_name = "themes"
#     template_name = "cours/home.html"


    
    
def home(request):
    themes = Theme.objects.all().order_by('-date')
    cats = Category.objects.all()
    p = Paginator(cats, 10)
    page = request.GET.get('categorie')
    cat = p.get_page(page)
    
    context = {
        "themes" : themes,
        'cat':cat,
    }
    return render(request, 'cours/home.html', context)


def cat(request):
    cat = Category.objects.all().order_by('nom')
    

    return render(request, 'cours/toutcat.html', locals())

# -----------------Voir un seul theme et ses détails------------------

@login_required(redirect_field_name="/cours/login/")
def themedetail(request, slug):
    the = Theme.objects.all()
    theme = Theme.objects.get(slug=slug)
    commentaires = theme.commentaire_set.all()
    cats = Category.objects.all()
    p = Paginator(cats, 10)
    page = request.GET.get('categorie')
    cat = p.get_page(page)
        
    if request.method == 'POST':
        user = request.user
        theme_id = request.POST['theme_id']
        identifiant = request.POST['identifiant']
        prix = request.POST['prix']
        
        ident = historique.objects.filter(user=user)
        for i in ident:
            if identifiant == i.identifiant:
                break
        else:
            story = historique(user=user, theme_id=theme_id, identifiant=identifiant, prix=prix)
            story.save()
                
        
        
        return redirect(f"../../lessonvideo/{identifiant}")
    
    
    
   
    context = {
        "theme" : theme,
        "commentaires": commentaires,
        'cat': cat,
    }
    
    return render(request, 'cours/themedetail.html', context)

# ----------------------afficher par catégorie--------------------------

def parCategorie(request, slug):
    categorie = Category.objects.get(slug=slug)
    themes = categorie.theme_set.all()
    cats = Category.objects.all()
    p = Paginator(cats, 10)
    page = request.GET.get('categorie')
    cat = p.get_page(page)
    
    
    
    
    # context = {
    #     "themes": themes,
    #     "categorie":categorie
    # }
    
    return render(request, 'cours/parcategorie.html', locals())



# --------------------Afficher story utilisateurs--------------------------

def listestory(request):
    stories = historique.objects.filter(user = request.user).order_by('-date')
    
    return render(request, 'cours/listestory.html' , locals())



# -----------------Voir un seul cours et ses détails------------------
@login_required(redirect_field_name="/cours/login/")
def seeTheme(request, slug):
    theme = Theme.objects.get(slug=slug)
    return render(request, 'cours/test/theme.html', locals())

    
# -------------------afficher la liste des cours-----------------
def liste(request):
    themes = Theme.objects.all().order_by('-date')
    cats = Category.objects.all()
    p = Paginator(cats, 10)
    page = request.GET.get('categorie')
    cat = p.get_page(page)
    
    context = {
        "themes" : themes,
        'cat': cat,
    }
    return render (request, 'cours/liste.html', context)

# --------------------------------------userlesson theme ----------------
@login_required(redirect_field_name="/cours/login/")
def user_liste(request):
    themes = Theme.objects.all().order_by('-date')
    cats = Category.objects.all()
    p = Paginator(cats, 10)
    page = request.GET.get('categorie')
    cat = p.get_page(page)
    
    context = {
        "themes" : themes,
        'cat': cat,
    }
    return render (request, 'cours/use_liste.html', context)



# ----------------------------------supprimer ------------------------------------

class supp(DeleteView):
    model = Theme
    context_object_name = "theme"
    template_name = "cours/supprimer.html"
    def get_success_url(self):
        
        return reverse(user_liste)
    


# ----------------------------afficher le profil d'un professeur---------------


def showprofile(request, slug):
    professeur = User.objects.get(username=slug)
    theme = professeur.theme_set.all()
    cats = Category.objects.all()
    p = Paginator(cats, 10)
    page = request.GET.get('categorie')
    cat = p.get_page(page)
    
    return render(request, 'cours/showprofile.html', locals())




# -------------------------------lesson en video------------------

@login_required(redirect_field_name="/cours/login/")
def lessonvideo(request, slug):
    cours = "9b05-48ca0f986dc5?a507b98e-6464-4679-8587-41a6c8141d8b"
    theme = Theme.objects.get(identifiant=slug)
    commentaires = theme.commentaire_set.all()
    
    if request.method == "POST":
        form = CommentaireForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.theme = theme
            form.save()
            return redirect(f'../../lessonvideo/{slug}')
    else:
        form = CommentaireForm()
    
    context = {
        'theme':theme, 
        'cours': cours,
        "commentaires": commentaires,
        "form" : form,
        'cat': cat,
        }
    
    return render(request, 'cours/lessonvideo.html', context)

# -------------------ENREGISTREMENT-----------------------------

def register(request):
    cats = Category.objects.all()
    p = Paginator(cats, 10)
    page = request.GET.get('categorie')
    cat = p.get_page(page)
    
    

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            messages.success(request, "User has been registred")
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
        return redirect('etudiant')
    else:
        form = UserCreationForm()
        
    return render(request, 'cours/register.html', locals())

# ----------------------------modifier_____________________________________________

class update_lesson(UpdateView):
    model = Theme
    fields = ('title', 'description', "miniature", "video", "prix", 'document_pdf', 'niveau', "categorie", 'timing')
    context_object_name = "themes"
    template_name = "cours/update_cours.html"
    def get_success_url(self):
        return reverse(user_liste)   
    
     




# -------------------------login----------------------------

def connexion(request):
    error = False
    cats = Category.objects.all()
    p = Paginator(cats, 10)
    page = request.GET.get('categorie')
    cat = p.get_page(page)

    if request.method == 'POST':
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            if user := authenticate(username=username, password=password):
                login(request, user)
                return redirect('home')
            else:
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'cours/connexion.html', locals())

# --------------------------Ajouter un theme ------------------------------------------

@login_required(redirect_field_name="/cours/login/")
def add_theme(request):
    if request.method == 'POST':
        form = add_themeForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.auteur = request.user
            form.save()
            return redirect(reverse(user_liste))
        else:
            error = True
    else:
        form = add_themeForm()
    return render(request, 'cours/add_theme.html', locals())

    
    

# -------------------------------Ajouter un cours ----------------------------------------









# --------------------------créer deu profil------------------------
@login_required(redirect_field_name="/cours/login/")
def Etudiant(request):
    if request.method == 'POST':
        form = ProfilForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect(reverse(home))
    else:
        form = ProfilForm()
    
    return render(request, 'cours/etudiant.html', locals())
            

def deconnexion(request):
    logout(request)
    return redirect('home')


# -----------------------------recherche-------------------------
def recherche(request):
    search = request.GET.get('search')
    themes = Theme.objects.filter(Q(title__icontains=search) | Q(description__icontains=search))
    
    
  
    return render(request, 'cours/recherche.html', locals())





# ------------------------about----------------------------
def about(request):
    perso =profil.objects.all()
    
    cats = Category.objects.all()
    p = Paginator(cats, 10)
    page = request.GET.get('categorie')
    cat = p.get_page(page)
    
    
    if request.method == 'POST':
        test = False
        form = emailForm(request.POST)
        if form.is_valid():
            form.save()
            test = True
            return redirect(reverse(about))
        
    else:
        form = emailForm()
    
    
    
    return render(request, 'cours/about.html', locals())


# ----------------------------devenir prof ----------------------

@login_required(redirect_field_name="/cours/login/")
def demande(request):
    if request.method == 'POST':
        form = demandeForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect(reverse(merci))
    else:
        form = demandeForm()
    
    return render(request, 'cours/demande.html', locals())

def merci(request):
    return render(request, 'cours/merci.html', locals())

# ----------------------partie des commentaire ---------------------


# def applesson(request, slug):
#     theme = Theme.objects.get(slug=slug)
#     lesson = theme.lesson_set.get(slug=slug)
#     return render(request, 'cours/test/index.html', locals())
 






