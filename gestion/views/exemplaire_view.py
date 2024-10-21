from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from gestion.models.exemplaire import Exemplaire
from gestion.permissions import IsEditorUser, IsAdminUser
from gestion.serializers import ExemplaireSerializer

class ExemplaireViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser, IsEditorUser]
    queryset = Exemplaire.objects.all()
    serializer_class = ExemplaireSerializer
