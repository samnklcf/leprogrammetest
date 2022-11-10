from time import sleep
from django.urls import path
from .views import *
import uuid




urlpatterns = [
    path('', home, name="home"),
    # path("theme/<str:slug>", ListeLesson, name="lesson"),
    
    
    # path("app/<int:id>/", applesson, name="applesson"),
    path("test/<str:slug>", seeTheme, name="cours"),
    path('liste/theme/<str:slug>', themedetail, name="themedetail"),
    path('liste/', liste, name="liste"),
    path('liste/categorie/<str:slug>/', parCategorie, name="categorie"),
    path("lessonvideo/<str:slug>/", lessonvideo, name="lessonvideo"),
    path("lesson/categorie/", cat, name="toutcat"),
    path("enregistrement/", register, name="register"),
    path("login/", connexion, name="login"),
    path("deconnexion/", deconnexion, name="deconnexion"),
    path('etudiant/', Etudiant, name="etudiant"),
    path('merci/', merci, name="merci"),
    path('demande/', demande, name="demande"),
    path("ajouter/theme/", add_theme, name="add_theme"),
    path("misajour/theme/<str:slug>", update_lesson.as_view(), name="maj"),
    path('liste/mespostes', user_liste, name="use_liste"),
    path('liste/supprimer/<str:slug>', supp.as_view(), name="supp"),
    path('apropos/', about, name="about"),
    path('story/', listestory, name="story"),
    path('professeur/profil/<str:slug>', showprofile, name="showprofile"),
    path('recherche', recherche, name="recherche"),
   

    
    
    # re_path(r"^/categorie/(?P<slug>[-\w])*$", voir, name="categorie"),

    
]