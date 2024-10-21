from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from gestion.models.commentaire import Commentaire
from gestion.serializers import CommentaireSerializer

class CommentaireViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer
