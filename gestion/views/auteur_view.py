from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from gestion.models.auteur import Auteur
from gestion.serializers import AuteurSerializer

class AuteurViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Auteur.objects.all()
    serializer_class = AuteurSerializer
