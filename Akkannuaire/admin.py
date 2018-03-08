from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

@admin.register(Consultant)
class ConsultantAdmin(admin.ModelAdmin):
    pass

@admin.register(Administrateur)
class ConsultantAdmin(admin.ModelAdmin):
    pass

@admin.register(BusinessManager)
class BusinessManagerAdmin(admin.ModelAdmin):
    pass

@admin.register(ControleurDeGestion)
class ControleurDeGestionAdmin(admin.ModelAdmin):
    pass

@admin.register(ChargeDeRecrutement)
class ChargeDeRecrutementAdmin(admin.ModelAdmin):
    pass

@admin.register(ResponsableRessourceHumaine)
class ResponsableRessourceHumaineAdmin(admin.ModelAdmin):
    pass

@admin.register(AssistantAgence)
class AssistantAgenceAdmin(admin.ModelAdmin):
    pass

@admin.register(Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    pass