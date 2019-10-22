from django.shortcuts import render
from .models import Product
# Create your views here.

def product(request):
    object_list = Product.objects.all()
    print('\n\n',object_list)
    return render(request, 'product/product.html', {'objetos':object_list})
