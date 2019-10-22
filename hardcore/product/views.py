from django.shortcuts import render
from .models import Product
# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse

def product(request):
    object_list = Product.objects.all()
    return render(request, 'product/product.html', {'objetos':object_list})

def edit(request, id):
    if request.POST:
        description = request.POST['description']
        name = request.POST['name']
        value = request.POST['value']
        product = Product.objects.get(id =id)
        product.name = name
        product.description = description
        product.description = value
        product.save()
        return HttpResponseRedirect(reverse('product:index'))
    return render(request, 'product/edit.html' )
