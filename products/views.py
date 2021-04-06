from django.shortcuts import render
from .models import Product

# Create your views here.

def all_products(request):
    """ A view to show all products, includes sorting and searh and queris """

    products = Product.objects.all()

    context = {
        'products': products,
    }
   
    return render(request, 'products/products.html', context)