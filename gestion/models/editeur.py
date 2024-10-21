from django.db import models

class Editeur(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    site_web = models.URLField()
    email_contact = models.EmailField()
    description = models.TextField()
    logo = models.TextField()

    def __str__(self):
        return self.nom
