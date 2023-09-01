from django.db import models
from category.models import Category
# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    product_description = models.TextField(max_length=500, blank=True, null=True)
    price = models.IntegerField(blank=False, null=False)
    stock = models.IntegerField(blank=False, null=False)
    is_available = models.BooleanField(default=True)
    images = models.ImageField(upload_to='photos/products')
    create_date = models.DateField(auto_now=False, auto_now_add=True)
    modified_date = models.DateField(auto_now=True, auto_now_add=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.product_name