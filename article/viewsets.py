from rest_framework import viewsets, filters
from .models import Article, Book, Product
from .serializers import ArticleSerializer, BookSerializer, ProductSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('article_id', 'article_heading', 'article_body')


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('book_id', 'book_name', 'book_author', 'book_description')


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('product_id', 'product_name', 'product_description', 'product_price')