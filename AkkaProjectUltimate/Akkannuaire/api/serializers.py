from rest_framework.serializers import *
from Akkannuaire.models import *

class BusinessManagerSerializer(ModelSerializer):
    class Meta:
        model = BusinessManager
        fields = "__all__"
        depth = 4

class ChargeDeRecrutementSerializer(ModelSerializer):
    class Meta:
        model = ChargeDeRecrutement
        fields = "__all__"
        depth = 4