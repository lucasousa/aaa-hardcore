from django.shortcuts import render
from .models import Product
from .models import AAA
# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    object_list = Product.objects.all()
    if("busca" in request.GET):
        object_list = object_list.filter(name__icontains=request.GET["busca"])
    return render(request, 'product/product.html', {'objetos':object_list})

def add(request):
    if request.POST:
        logo = request.FILES['image']
        description = request.POST['description']
        name = request.POST['name']
        value = request.POST['value']
        athletic = AAA.objects.get(id=1)
        product = Product.objects.create(name = name, image = logo, value= value, description = description,athletic= athletic )
        product.save()
        return HttpResponseRedirect(reverse('product:index'))
    return render(request, 'product/add.html')

def edit(request, id):
    if request.POST:
        description = request.POST['description']
        name = request.POST['name']
        value = request.POST['value']
        product = Product.objects.get(id =id)
        product.name = name
        product.description = description
        product.value = value
        product.save()
        return HttpResponseRedirect(reverse('product:index'))
    return render(request, 'product/edit.html', {'objeto':Product.objects.get(id=id)} )

def delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return HttpResponseRedirect(reverse('product:index'))

def views_product(request,id):
    product = Product.objects.get(id=id)
    res = {
        'objeto':product
    }
    return render(request,'product/product_detail.html',res)