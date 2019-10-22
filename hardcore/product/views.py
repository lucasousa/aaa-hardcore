from django.shortcuts import render
from .models import Product
# Create your views here.

def product(request):
    object_list = Product.objects.all()
    return render(request, 'product/product.html', {'objetos':object_list})
