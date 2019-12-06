from django.shortcuts import render
from .models import Association
from aaa.models import AAA
from django.contrib.auth.models import User 
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
import datetime

# Create your views here.

def index(request):
    object_list = User.objects.all()

    if 'filter' in request.GET and request.GET['filter'] == 'not-associated':
        object_list = sorted(object_list, key=lambda t: t.profile.has_associated)
        print("=========== object list", object_list)

    if("busca" in request.GET):
        object_list = object_list.filter(name__icontains=request.GET["busca"])
    return render(request, 'association/manage-association.html', {'objetos':object_list})

def add(request):
    usuario = User.objects.get(id=request.GET['data'])
    atletica = AAA.objects.get(id=1)
    expiration_date = datetime.date.today().replace(year=datetime.date.today().year + 1)
    association = Association.objects.create(expiration_date = expiration_date, user=usuario, athletic = atletica)
    association.save()
    return JsonResponse({'mensagem': "Associação criada com sucesso!", 'code': "1"})
    

def deletar(request, id):
    association = Association.objects.get(id=id)
    association.delete()
    return HttpResponseRedirect(reverse('association:index'))