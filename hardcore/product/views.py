from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.conf import settings
from django.urls import reverse
from .models import Product
from django.contrib import messages
from .models import AAA
import os


@login_required
def index(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('core:my-association'))
    object_list = Product.objects.all()
    if("busca" in request.GET):
        object_list = object_list.filter(name__icontains=request.GET["busca"])
    return render(request, 'product/product.html', {'objetos': object_list})


@login_required
def add(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('core:my-association'))
    if request.POST:
        logo = request.FILES['image']
        description = request.POST['description']
        name = request.POST['name']
        value = request.POST['value']
        athletic = AAA.objects.get(id=1)
        product = Product.objects.create(
            name=name, image=logo, value=value, description=description, athletic=athletic)
        product.save()
        
        messages.success(request, 'Produto adicionado com sucesso!')
        return HttpResponseRedirect(reverse('product:index'))
    return render(request, 'product/add.html')


@login_required
def edit(request, id):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('core:my-association'))
    if request.POST:
        description = request.POST['description']
        name = request.POST['name']
        value = request.POST['value']
        product = Product.objects.get(id=id)
        product.name = name
        product.description = description
        product.value = value
        if 'logo' in request.FILES:
            logo = request.FILES['logo']
            old_file = settings.MEDIA_ROOT + str(product.image)
            try:
                os.remove(old_file)
            except:
                pass

            product.image = logo

        product.save()
        messages.success(request, 'Produto editado com sucesso!')
        return HttpResponseRedirect(reverse('product:index'))
    return render(request, 'product/edit.html', {'objeto': Product.objects.get(id=id)})


@login_required
def delete(request, id):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('core:my-association'))
    product = Product.objects.get(id=id)
    product.delete()
    return JsonResponse({'msg': "Produto excluído com sucesso!", 'code': "1"})


def views_product(request, id):
    product = Product.objects.get(id=id)
    res = {
        'objeto': product
    }
    return render(request, 'product/product_detail.html', res)
