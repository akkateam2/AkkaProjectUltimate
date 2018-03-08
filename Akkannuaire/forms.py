from django import forms
from .models import *

class UtilisateurForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['nom', 'prenom', 'mdp', 'type', "superieur"]
        widgets = {
            "nom": forms.TextInput(attrs={"class": "form-control", "id": "nom"}),
            "prenom": forms.TextInput(attrs={"class": "form-control", "id": "prenom"}),
            "mdp": forms.TextInput(attrs={"class": "form-control", "id": "mdp"}),
            "superieur": forms.TextInput(attrs={"class": "form-control", "ng-model": "superieurModel", "id":"superieur_id"}),
            "type": forms.Select(
                attrs={
                    "class": "form-control",
                    "id": "type",
                    "ng-model":"type",
                    "ng-click":"clickChoixType()"
                })
        }

class ConsultantForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ConsultantForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            if field.label in ["ChargeDeRecrutement", "AssistantDAgence", "BusinessManager"]:
                field.widget.attrs['class'] = 'form-control select2'
            else:
                if field.label in ["DateNaissance", "DateEntreeDansLeGroupe", "DateValiditeTitreDeSejour"]:
                    field.widget.attrs['class'] = 'form-control pull-right'
                else:
                    if field.label != "Francais":
                        if field.label != "Photo" and field.label != "Cv":
                            field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Consultant
        fields = [
            'nom',
            'cv',
            'photo',
            'prenom',
            'businessManager',
            'chargeDeRecrutement',
            "assistantDAgence",
            "niveauDiplome",
            "anneeExperience",
            "ville",
            "codePostal",
            "adresse",
            "telephone",
            "dateNaissance",
            "dateEntreeDansLeGroupe",
            "francais",
            "dateValiditeTitreDeSejour",
            "salaire",
        ]