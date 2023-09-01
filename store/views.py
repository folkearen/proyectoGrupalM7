from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Product, Category

# Create your views here.

def home(request, category_slug=None):
    categoires = None
    products = None
    if category_slug != None:
        categoires = Category.objects.all()
        categories_searh = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories_searh,is_available=True)
        return render(request, 'store/home.html', {
            'categories' : categoires,
            'products' : products
        })

    categoires = Category.objects.all()
    products = Product.objects.filter(is_available=True)
    return render(request, 'store/home.html', {
        'categories' : categoires,
        'products' : products
    })