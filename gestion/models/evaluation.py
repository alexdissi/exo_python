from django.db import models
from django.contrib.auth.models import User
from .livre import Livre

class Evaluation(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    note = models.IntegerField()
    commentaire = models.TextField()
    date_evaluation = models.DateTimeField(auto_now_add=True)
    recommande = models.BooleanField(default=False)
    titre = models.CharField(max_length=255)

    def __str__(self):
        return f"Évaluation de {self.utilisateur.username} pour {self.livre.titre}"
