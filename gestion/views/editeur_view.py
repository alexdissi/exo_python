from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from gestion.models.editeur import Editeur
from gestion.serializers import EditeurSerializer

class EditeurViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Editeur.objects.all()
    serializer_class = EditeurSerializer
