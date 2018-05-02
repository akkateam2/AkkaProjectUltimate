from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.db.models import Q
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='/login/')
def home(request):
    return render(request, 'base.html')

# @login_required(login_url='/login/')
def login(request):
    return render(request, 'registration/login.html')

# @login_required(login_url='/login/')
def consultant_liste(request):
    consultants = Consultant.objects.all()
    content = {
        "consultants": consultants
    }

    return render(request, 'consultant_liste.html', content)

# @login_required(login_url='/login/')
def consultant_detail(request, idConsultant=None):
    consultant = Consultant.objects.filter(id=idConsultant).first()
    content = {
        "consultant":consultant,
    }
    return render(request, 'consultant_detail.html', content)

# @login_required(login_url='/login/')
def consultant_modifier(request, idConsultant=None):
    consultant = Consultant.objects.filter(id=idConsultant).first()
    form = ConsultantForm(
        request.POST or None,
        request.FILES or None,
        instance=consultant,
        initial={
            'businessManager':consultant.businessManager,
            'chargeDeRecrutement':consultant.chargeDeRecrutement,
            'assistantDAgence':consultant.assistantDAgence,
        })
    if request.POST:
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('consultant-liste')
    content = {
        "form": form
    }
    return render(request, 'consultant_modifier.html', content)

# @login_required(login_url='/login/')
def consultant_creer(request):
    form = ConsultantForm(request.POST or None, request.FILES)
    if request.POST:
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('consultant-liste')
    content = {
        "form": form
    }
    return render(request, 'consultant_creer.html', content)

# @login_required(login_url='/login/')
def utilisateur_liste(request):
    users = Utilisateur.objects.all()
    for user in users:
        user.get_superieur()
    content = {
        "users": users
    }
    return render(request, 'utilisateur_liste.html', content)

# @login_required(login_url='/login/')
def utilisateur_detail(request, idUser=None):
    utilisateur = Utilisateur.objects.filter(id=idUser).first()
    utilisateur.get_superieur()
    consultants = Consultant.objects.filter(
        Q(businessManager__user=utilisateur.user)|
        Q(chargeDeRecrutement__user=utilisateur.user)|
        Q(assistantDAgence__user=utilisateur.user)
    )
    content = {
        "utilisateur": utilisateur,
        "consultants": consultants
    }
    return render(request, 'utilisateur_detail.html', content)

# @login_required(login_url='/login/')
def utilisateur_modifier(request, idUser=None):
    utilisateur = Utilisateur.objects.filter(id=idUser).first()
    utilisateur.get_superieur()
    form = UtilisateurForm(instance=utilisateur)
    if request.POST:
        form = UtilisateurForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            username = instance.prenom[0] + instance.nom
            string = username.split(' ')
            username = '-'.join(string)
            user = User.objects.create_user(
                username=username,
                password="12345678",
                email="hello@la.com",
                first_name=instance.nom,
                last_name=instance.prenom,
                instance_type = instance.type 
            )
            user.is_staff = True
            user.save()

            if instance.type == "Chargé de recrutement":
                cr = ChargeDeRecrutement()
                cr.nom = instance.nom
                superieur = ChargeDeRecrutement.objects.filter(id=instance.superieur).first()
                if superieur:
                    cr.parent = superieur
                cr.prenom = instance.prenom
                cr.type = instance.type
                cr.mdp = instance.mdp
                cr.superieur = "---"
                cr.user = user
                cr.save()
            if instance.type == "Business Manager":
                bm = BusinessManager()
                superieur = BusinessManager.objects.filter(id=int(instance.superieur)).first()
                if superieur:
                    bm.parent = superieur
                bm.nom = instance.nom
                bm.prenom = instance.prenom
                bm.type = instance.type
                bm.mdp = instance.mdp
                bm.user = user
                bm.superieur = "---"
                bm.save()
            if instance.type == "Assistant d'agence":
                aa = AssistantAgence()
                aa.nom = instance.nom
                aa.prenom = instance.prenom
                aa.type = instance.type
                aa.mdp = instance.mdp
                aa.user = user
                aa.save()
            if instance.type == "Responsable des ressources humaines":
                rrh = ResponsableRessourceHumaine()
                rrh.nom = instance.nom
                rrh.prenom = instance.prenom
                rrh.type = instance.type
                rrh.mdp = instance.mdp
                rrh.user = user
                rrh.save()
            if instance.type == "Contrôleur de gestion":
                cg = ControleurDeGestion()
                cg.nom = instance.nom
                cg.prenom = instance.prenom
                cg.type = instance.type
                cg.mdp = instance.mdp
                cg.user = user
                cg.save()
            if instance.type == "Administrateur":
                admin = Administrateur()
                admin.nom = instance.nom
                admin.prenom = instance.prenom
                admin.type = instance.type
                admin.mdp = instance.mdp
                admin.user = user
                admin.save()
            return redirect('utilisateur-liste')
    content = {
        "form": form,
    }
    return render(request, 'utilisateur_modifier.html', content)

# @login_required(login_url='/login/')
def utilisateur_creer(request):
    form = UtilisateurForm()
    if request.POST:
        form = UtilisateurForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            username = instance.prenom[0] + instance.nom
            string = username.split(' ')
            username = '-'.join(string)
            user = User.objects.create_user(
                username=username,
                password="12345678",
                email="hello@la.com",
                first_name=instance.nom,
                last_name=instance.prenom,
                instance_type = instance.type
            )
            user.is_staff = True
            user.save()

            if instance.type == "Chargé de recrutement":
                cr = ChargeDeRecrutement()
                cr.nom = instance.nom
                if instance.superieur:
                    superieur = ChargeDeRecrutement.objects.filter(id=instance.superieur).first()
                    if superieur:
                        cr.parent = superieur
                cr.prenom = instance.prenom
                cr.type = instance.type
                cr.mdp = instance.mdp
                cr.superieur = "---"
                cr.user = user
                cr.save()
            if instance.type == "Business Manager":
                bm = BusinessManager()
                if instance.superieur:
                    superieur = BusinessManager.objects.filter(id=int(instance.superieur)).first()
                    if superieur:
                        bm.parent = superieur
                bm.nom = instance.nom
                bm.prenom = instance.prenom
                bm.type = instance.type
                bm.mdp = instance.mdp
                bm.user = user
                bm.superieur = "---"
                bm.save()
            if instance.type == "Assistant d'agence":
                aa = AssistantAgence()
                aa.nom = instance.nom
                aa.prenom = instance.prenom
                aa.type = instance.type
                aa.mdp = instance.mdp
                aa.user = user
                aa.save()
            if instance.type == "Responsable des ressources humaines":
                rrh = ResponsableRessourceHumaine()
                rrh.nom = instance.nom
                rrh.prenom = instance.prenom
                rrh.type = instance.type
                rrh.mdp = instance.mdp
                rrh.user = user
                rrh.save()
            if instance.type == "Contrôleur de gestion":
                cg = ControleurDeGestion()
                cg.nom = instance.nom
                cg.prenom = instance.prenom
                cg.type = instance.type
                cg.mdp = instance.mdp
                cg.user = user
                cg.save()
            if instance.type == "Administrateur":
                admin = Administrateur()
                admin.nom = instance.nom
                admin.prenom = instance.prenom
                admin.type = instance.type
                admin.mdp = instance.mdp
                admin.user = user
                admin.save()
            return redirect('utilisateur-liste')
    content = {
        "form": form,
    }
    return render(request, 'utilisateur_creer.html', content)