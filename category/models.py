from django.db import models
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    description  = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True)
    category_image = models.ImageField(upload_to = 'photos/categories', blank=True)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'



    def __str__(self):
        return self.category_name
    #slug
    # El slug_field se usa en combinación con el slug del modelo,
    #  que es un campo adicional que almacena el valor del "slug". Django genera automáticamente el valor del
    #  "slug" a partir del contenido del campo especificado en slug_field. El objetivo principal del "slug" 
    # es proporcionar una URL amigable para el usuario, ya que suele estar en minúsculas, sin espacios y con 
    # caracteres especiales reemplazados por guiones o guiones bajos.