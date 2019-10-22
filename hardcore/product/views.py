from django.shortcuts import render
from .models import Product
# Create your views here.

def product(request):
    # object_list = Product.objects.all()
    # context = {
    #     'product_list':object_list,
    # }
    return render(request,'product/product.html')
