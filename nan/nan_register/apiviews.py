from rest_framework import viewsets, filters
from .models import *
from .serializers import *
from drf_dynamic_fields import DynamicFieldsMixin

class PaysViewSet(viewsets.ModelViewSet):
   # filter_backends = (DynamicSearchFilter,)
    queryset = Pays.objects.filter(statut=True)
    serializer_class = PaysSerializer


class VilleViewSet(viewsets.ModelViewSet):
    #filter_backends = (DynamicSearchFilter,)
    queryset = Ville.objects.filter(statut=True)
    serializer_class = VilleSerializer


class CommuneViewSet(viewsets.ModelViewSet):
   # filter_backends = (DynamicSearchFilter,)
    queryset = Commune.objects.filter(statut=True)
    serializer_class = CommuneSerializer