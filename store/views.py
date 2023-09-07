from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Product, Category
from django.db.models import Q
from django.http import JsonResponse
# Create your views here.

def home(request, category_slug=None):
    categoires = Category.objects.all()
    products = Product.objects.filter(is_available=True)
    busqueda = request.GET.get("buscar")

    if category_slug:
        categories_search = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=categories_search)

    if busqueda:
        products = products.filter(
            Q(product_name__icontains=busqueda) |
            Q(product_description__icontains=busqueda)
        ).distinct()

    return render(request, 'store/home.html', {
        'categories': categoires,
        'products': products,
        'busqueda': busqueda
    })

def detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)

    context = {'product': product}
    return render(request, 'store/detail.html', context)