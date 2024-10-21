from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from gestion.models.emprunt import Emprunt
from gestion.permissions import IsAdminUser, IsEditorUser
from gestion.serializers import EmpruntSerializer

class EmpruntViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser, IsEditorUser]
    queryset = Emprunt.objects.all()
    serializer_class = EmpruntSerializer