from django.shortcuts import render

# Create your views here.

from .models import Product

def products_list(request):
    products = Product.objects.all()
    return render(request, 'catalogue/products_list.html', {'products': products})

def products_details(request):
    product = Product.objects.get(id=product_id)
    return render(request, 'catalogue/products_details.html', {"products": products})

