from django.db import models
from django.contrib.auth.models import User

# Create your models here.
BM = "Business Manager"
CdR = "Chargé de recrutement"
AdA = "Assistant d'agence"
RRH = "Responsable des ressources humaines"
CG = "Contrôleur de gestion"
ADMIN = "Administrateur"

TYPE = (
    (BM, "Business Manager"),
    (CdR, "Chargé de recrutement"),
    (AdA, "Assistant d'agence"),
    (RRH, "Responsable des ressources humaines"),
    (CG, "Contrôleur de gestion"),
    (ADMIN, "Administrateur"),
)

class Utilisateur(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    mdp = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=TYPE)
    superieur = models.CharField(max_length=100, null=True, blank=True)

    @property
    def full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.nom, self.prenom)

    def get_superieur(self):
        "Returns the person's full name."
        if self.type == "Business Manager":
            sup = BusinessManager.objects.filter(user=self.user).first()
            if sup and sup.parent:
                self.superieur = sup.parent.full_name

        if self.type == "Chargé de recrutement":
            sup = ChargeDeRecrutement.objects.filter(user=self.user).first()
            if sup and sup.parent:
                self.superieur = sup.parent.full_name

    def __str__(self):
        return "{} {}".format(self.nom, self.prenom)
class BusinessManager(Utilisateur):
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.DO_NOTHING)

class AssistantAgence(Utilisateur):
    pass

class Administrateur(Utilisateur):
    pass

class ResponsableRessourceHumaine(Utilisateur):
    pass

class ChargeDeRecrutement(Utilisateur):
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.DO_NOTHING)

class ControleurDeGestion(Utilisateur):
    pass

class Consultant(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    businessManager = models.ForeignKey(BusinessManager, on_delete=models.DO_NOTHING)
    chargeDeRecrutement = models.ForeignKey(ChargeDeRecrutement, on_delete=models.DO_NOTHING)
    assistantDAgence = models.ForeignKey(AssistantAgence, on_delete=models.DO_NOTHING)
    dateNaissance = models.DateField()
    photo = models.ImageField(upload_to='uploads/')
    cv = models.FileField(upload_to='uploads/')
    dateEntreeDansLeGroupe = models.DateField()
    francais = models.BooleanField()
    dateValiditeTitreDeSejour = models.DateField()
    salaire = models.IntegerField()
    telephone = models.IntegerField()
    adresse = models.CharField(max_length=150)
    codePostal = models.IntegerField()
    ville = models.CharField(max_length=100)
    anneeExperience = models.IntegerField()
    niveauDiplome = models.CharField(max_length=100)