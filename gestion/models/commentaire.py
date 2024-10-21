from django.db import models
from django.contrib.auth.models import User
from .livre import Livre

class Commentaire(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    note = models.IntegerField()
    visible = models.BooleanField(default=True)
    modere = models.BooleanField(default=False)

    def __str__(self):
        return f"Commentaire de {self.utilisateur.username} sur {self.livre.titre}"
