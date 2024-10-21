from django.db import models
from django.contrib.auth.models import User
from .exemplaire import Exemplaire

class Emprunt(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    exemplaire = models.ForeignKey(Exemplaire, on_delete=models.CASCADE)
    date_emprunt = models.DateTimeField(auto_now_add=True)
    date_retour_prevue = models.DateTimeField()
    date_retour_effective = models.DateTimeField(null=True, blank=True)
    statut = models.CharField(max_length=50)
    remarques = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Emprunt de {self.exemplaire.livre.titre} par {self.utilisateur.username}"
