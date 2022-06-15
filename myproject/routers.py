from rest_framework import routers
from article.viewsets import ArticleViewSet, BookViewSet, ProductViewSet

router = routers.DefaultRouter()

router.register(r'article', ArticleViewSet)
router.register(r'book', BookViewSet)
router.register(r'product',ProductViewSet)
