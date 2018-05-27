from django.db import models
from django.contrib.auth.models import User





# Create your models here.
BM = "Business Manager"
CdR = "Chargé de recrutement"
AdA = "Assistant d'agence"
RRH = "Responsable des ressources humaines"
CG = "Contrôleur de gestion"
ADMIN = "Administrateur"

B2MOIN = "Niveau B+2/3 ou inférieur"
B23 = "B+2/3"
B5 = "B+5"
B7 = "B+7 ou plus"

NIVEAU = (
    (B2MOIN, "Niveau B+2/3 ou inférieur"),
    (B23, "B+2/3"),
    (B5, "B+5"),
    (B7, "B+7 ou plus"),
)

TYPE = (
    (BM, "Business Manager"),
    (CdR, "Chargé de recrutement"),
    (AdA, "Assistant d'agence"),
    (RRH, "Responsable des ressources humaines"),
    (CG, "Contrôleur de gestion"),
    (ADMIN, "Administrateur"),
)

class Utilisateur(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
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
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)

class AssistantAgence(Utilisateur):
    pass

class Administrateur(Utilisateur):
    pass

class ResponsableRessourceHumaine(Utilisateur):
    pass

class ChargeDeRecrutement(Utilisateur):
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)

class ControleurDeGestion(Utilisateur):
    pass

class Consultant(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    businessManager = models.ForeignKey(BusinessManager, on_delete=models.CASCADE, null=True, blank=True)
    chargeDeRecrutement = models.ForeignKey(ChargeDeRecrutement, on_delete=models.CASCADE, null=True, blank=True)
    assistantDAgence = models.ForeignKey(AssistantAgence, on_delete=models.CASCADE, null=True, blank=True)
    #dateNaissance = models.DateField(widget=forms.SelectDateWidget(years='1995'))
    dateNaissance= models.DateField(blank=True,null = True)
    #cur_year = datetime.datetime.today().year
    #year_range = tuple([i for i in range(cur_year - 2, cur_year + 2)])
    #dateNaissance = models.DateField(initial=datetime.date.today() - datetime.timedelta(days=7),widget=forms.SelectDateWidget(years=year_range))
    finPeriodeEssai = models.DateField(blank=True)
    photo = models.ImageField(upload_to='uploads/',null=True, blank=True, default ='uploads/Chrysanthemum.jpg')
    dossierCompetence = models.FileField(upload_to='uploads/',null=True, blank=True)
    cv = models.FileField(upload_to='uploads/', null=True, blank=True)
    dateEntreeDansLeGroupe = models.DateField(blank=True)
    francais = models.BooleanField()
    dateValiditeTitreDeSejour = models.DateField(null=True, blank=True)
    salaire = models.IntegerField()
    telephone = models.CharField(max_length=100, blank=True)
    emailAKKA = models.EmailField(null=True,max_length=254, blank=True)
    emailPerso = models.EmailField(null=True, blank=True)
    adresse = models.CharField(max_length=150, blank=True)
    codePostal = models.IntegerField(null=True, blank=True)
    ville = models.CharField(max_length=100, blank=True)
    anneeExperience = models.DateField(blank=True)
    niveauDiplome = models.CharField(max_length=100, choices=NIVEAU, default=B5)
    