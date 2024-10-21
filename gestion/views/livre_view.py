from guardian.shortcuts import get_objects_for_user
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from gestion.models.livre import Livre
from gestion.serializers import LivreSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from gestion.permissions import IsAdminUser, ObjectPermission

class CustomPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class LivreViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser, ObjectPermission]
    serializer_class = LivreSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['titre', 'langue', 'categorie', 'date_de_publication']
    ordering_fields = ['titre', 'date_de_publication', 'nombre_de_pages']
    ordering = ['titre']

    def get_queryset(self):
        return get_objects_for_user(self.request.user, 'view_livre', Livre)
