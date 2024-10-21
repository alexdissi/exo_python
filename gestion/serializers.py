from django.contrib.auth.models import Permission
from rest_framework import serializers
from .models.auteur import Auteur
from .models.livre import Livre
from .models.categorie import Categorie
from .models.exemplaire import Exemplaire
from .models.emprunt import Emprunt
from .models.commentaire import Commentaire
from .models.editeur import Editeur
from .models.evaluation import Evaluation

class AuteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auteur
        fields = '__all__'

class LivreSerializer(serializers.ModelSerializer):
    auteurs = AuteurSerializer(many=True)
    categorie = serializers.StringRelatedField()
    class Meta:
        model = Livre
        fields = '__all__'

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'

class ExemplaireSerializer(serializers.ModelSerializer):
    livre = LivreSerializer()
    class Meta:
        model = Exemplaire
        fields = '__all__'

class EmpruntSerializer(serializers.ModelSerializer):
    utilisateur = serializers.StringRelatedField()
    exemplaire = ExemplaireSerializer()
    class Meta:
        model = Emprunt
        fields = '__all__'

class CommentaireSerializer(serializers.ModelSerializer):
    utilisateur = serializers.StringRelatedField()
    livre = LivreSerializer()
    class Meta:
        model = Commentaire
        fields = '__all__'

class EditeurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editeur
        fields = '__all__'

class EvaluationSerializer(serializers.ModelSerializer):
    utilisateur = serializers.StringRelatedField()
    livre = LivreSerializer()
    class Meta:
        model = Evaluation
        fields = '__all__'

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'name', 'codename']
