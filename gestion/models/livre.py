from django.db import models
from .auteur import Auteur
from django.contrib.auth.models import User

class Livre(models.Model):
    titre = models.CharField(max_length=255)
    resume = models.TextField()
    date_de_publication = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    nombre_de_pages = models.IntegerField()
    langue = models.CharField(max_length=50)
    image_de_couverture = models.TextField()
    auteurs = models.ManyToManyField(Auteur)
    categorie = models.ForeignKey('Categorie', on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.titre
