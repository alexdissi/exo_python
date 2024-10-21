from django.db import models
from .livre import Livre

class Exemplaire(models.Model):
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    etat = models.CharField(max_length=50)
    date_acquisition = models.DateField()
    localisation = models.CharField(max_length=255)
    disponibilite = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.livre.titre} - {self.localisation}"
