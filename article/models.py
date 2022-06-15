import re
from django.db import models

# Create your models here.


class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    article_heading = models.CharField(max_length=250)
    article_body = models.TextField()

    def __str__(self):
        return self.article_heading

    class Meta:
        verbose_name_plural = 'Articles'


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100)
    book_description = models.TextField()

    def __str__(self):
        return self.book_name

    class Meta:
        verbose_name_plural = 'Book'


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name_plural = 'Products'
