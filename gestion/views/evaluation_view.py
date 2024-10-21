from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from gestion.models.evaluation import Evaluation
from gestion.permissions import IsEditorUser, IsAdminUser
from gestion.serializers import EvaluationSerializer

class EvaluationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser, IsEditorUser]
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
