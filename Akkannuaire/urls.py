from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('consultant/', views.consultant_liste, name="consultant-liste"),
    path('consultant/<int:idConsultant>/detail/', views.consultant_detail, name="consultant-detail"),
    path('consultant/creer/', views.consultant_creer, name="consultant-creer"),
    path('consultant/<int:idConsultant>/modifier/', views.consultant_modifier, name="consultant-modifier"),
    path('utilisateur/', views.utilisateur_liste, name="utilisateur-liste"),
    path('utilisateur/<int:idUser>/detail/', views.utilisateur_detail, name="utilisateur-detail"),
    path('utilisateur/creer/', views.utilisateur_creer, name="utilisateur-creer"),
    path('utilisateur/<int:idUser>/modifier/', views.utilisateur_modifier, name="utilisateur-modifier"),
]