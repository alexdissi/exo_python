from rest_framework.routers import DefaultRouter
from gestion.views.auteur_view import AuteurViewSet
from gestion.views.livre_view import LivreViewSet
from gestion.views.categorie_view import CategorieViewSet
from gestion.views.exemplaire_view import ExemplaireViewSet
from gestion.views.commentaire_view import CommentaireViewSet
from gestion.views.editeur_view import EditeurViewSet
from gestion.views.evaluation_view import EvaluationViewSet

router = DefaultRouter()
router.register(r'auteurs', AuteurViewSet, basename='auteur')
router.register(r'livres', LivreViewSet, basename='livre')
router.register(r'categories', CategorieViewSet, basename='categorie')
router.register(r'exemplaires', ExemplaireViewSet, basename='exemplaire')
router.register(r'commentaires', CommentaireViewSet, basename='commentaire')
router.register(r'editeurs', EditeurViewSet, basename='editeur')
router.register(r'evaluations', EvaluationViewSet , basename='evaluation')

urlpatterns = router.urls
