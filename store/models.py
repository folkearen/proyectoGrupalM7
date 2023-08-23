from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    product_description = models.TextField(max_length=500, blank=True, null=True)
    price = models.IntegerField()
    slug = models.SlugField(max_length=300, unique=True)