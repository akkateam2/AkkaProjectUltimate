from django.http import HttpResponse
from Akkannuaire.models import *
from django.core import serializers
from .serializers import *
import json
def get_bm_cdr_liste(request):
    type = request.GET.get('type', None)
    if type == "Business Manager":
        bms = BusinessManager.objects.all()
        data = BusinessManagerSerializer(bms, many=True).data
        content = {
            "superieurs": data
        }
    if type == "Chargé de recrutement":
        cdr = ChargeDeRecrutement.objects.all()
        data = ChargeDeRecrutementSerializer(cdr, many=True).data
        content = {
            "superieurs": data
        }
    return HttpResponse(json.dumps(content))