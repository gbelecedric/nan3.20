from drf_dynamic_fields import DynamicFieldsMixin
from rest_framework import serializers
from .models import * 

class CommuneSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    
    
    class Meta:
        model = Commune
        fields = '__all__'
        depth = 2

class VilleSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    commune_ville = CommuneSerializer(many=True, required=False)
    class Meta:
        model = Ville
        fields = '__all__'
        depth = 1

class PaysSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    pays_ville = VilleSerializer(read_only=True ,many=True)
    
    class Meta:
        model = Pays
        fields = '__all__'
        depth = 1
