from django.contrib import admin
from gestion.models.auteur import Auteur
from gestion.models.categorie import Categorie
from gestion.models.commentaire import Commentaire
from gestion.models.editeur import Editeur
from gestion.models.evaluation import Evaluation
from gestion.models.exemplaire import Exemplaire
from gestion.models.livre import Livre

admin.site.register(Auteur)
admin.site.register(Livre)
admin.site.register(Categorie)
admin.site.register(Exemplaire)
admin.site.register(Commentaire)
admin.site.register(Editeur)
admin.site.register(Evaluation)