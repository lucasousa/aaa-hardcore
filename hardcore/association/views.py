from django.shortcuts import render
from .models import Association
from aaa.models import AAA
from django.contrib.auth.models import User 
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    object_list = Association.objects.all()
    if("busca" in request.GET):
        object_list = object_list.filter(name__icontains=request.GET["busca"])
    return render(request, 'association/manage-association.html', {'objetos':object_list})

def add(request):
    if request.POST:
        entry_date = request.POST['associationdate']
        expiration_date = request.POST['expirationdate']
        email = request.POST['email']
        try:
            usuario = User.objects.get(email=email)
            atletica = AAA.objects.get(id=1)
            association = Association.objects.create(date_entry = entry_date, expiration_date = expiration_date, user=usuario, athletic = atletica)
            association.save()
        except:
            pass
        return HttpResponseRedirect(reverse('association:index'))
    return render(request, 'association/add.html')

def deletar(request, id):
    association = Association.objects.get(id=id)
    association.delete()
    return HttpResponseRedirect(reverse('association:index'))