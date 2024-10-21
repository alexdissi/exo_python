from django.db import models

class Auteur(models.Model):
    nom = models.CharField(max_length=255)
    biographie = models.TextField()
    date_de_naissance = models.DateField()
    date_de_deces = models.DateField(null=True, blank=True)
    nationalite = models.CharField(max_length=100)

    def __str__(self):
        return self.nom
