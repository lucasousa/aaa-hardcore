from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Association
from aaa.models import AAA
from django.contrib.auth.models import User
from django.urls import reverse
import datetime
from django.contrib import messages


@login_required
def index(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('core:my-association'))
    object_list = User.objects.all()

    if 'filter' in request.GET and request.GET['filter'] == 'not-associated':
        object_list = [x for x in object_list if not x.profile.has_associated]

    if("busca" in request.GET):
        object_list = object_list.filter(profile__full_name__icontains=request.GET["busca"])
    return render(request, 'association/manage-association.html', {'objetos': object_list})


@login_required
def add(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('core:my-association'))
    usuario = User.objects.get(id=request.GET['data'])
    atletica = AAA.objects.get(id=1)
    expiration_date = datetime.date.today().replace(
        year=datetime.date.today().year + 1)
    association = Association.objects.create(
        expiration_date=expiration_date, user=usuario, athletic=atletica)
    association.save()
    messages.success(request, 'Associação realizada com sucesso!')
    return JsonResponse({'mensagem': "Associação criada com sucesso!", 'code': "1"})


@login_required
def deletar(request, id):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('core:my-association'))

    user = User.objects.get(id=id)
    association = Association.objects.get(user=user)
    association.delete()
    return JsonResponse({'msg': "Associação excluída com sucesso!", 'code': "1"})