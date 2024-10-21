from guardian.shortcuts import get_objects_for_user
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from gestion.models.categorie import Categorie
from gestion.permissions import IsAdminUser
from gestion.serializers import CategorieSerializer

class CategorieViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

    def get_queryset(self):
        return get_objects_for_user(self.request.user, 'view_categorie', Categorie)