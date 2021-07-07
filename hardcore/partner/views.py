from django.shortcuts import render
from .models import Partner
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
import os
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
@login_required
def index(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('core:my-association'))
    object_list = Partner.objects.all()
    if("busca" in request.GET):
        object_list = object_list.filter(name__icontains=request.GET["busca"])
    return render(request, 'partner/manage-partner.html', {'objetos': object_list})


@login_required
def add(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('core:my-association'))
    if request.POST:
        logo = request.FILES['logo']
        description = request.POST['description']
        name = request.POST['name']
        value = request.POST['value']
        partner = Partner.objects.create(
            name=name, logo=logo,value=value, description=description)
        partner.save()
        messages.success(request, 'Parceiro cadastrado com sucesso!')
        return HttpResponseRedirect(reverse('partner:index'))
    return render(request, 'partner/add.html')


@login_required
def edit(request, id):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('core:my-association'))
    if request.POST:
        description = request.POST['description']
        name = request.POST['name']
        value = request.POST['value']
        partner = Partner.objects.get(id=id)
        partner.name = name
        partner.description = description
        partner.value = value
        if 'logo' in request.FILES:
            logo = request.FILES['logo']
            old_file = settings.MEDIA_ROOT + str(partner.logo)
            try:
                os.remove(old_file)
            except:
                pass

            partner.logo = logo

        partner.save()
        messages.success(request, 'Parceiro editado com sucesso!')
        return HttpResponseRedirect(reverse('partner:index'))
    return render(request, 'partner/edit.html', {'objeto': Partner.objects.get(id=id)})


@login_required
def deletar(request, id):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('core:my-association'))
    partner = Partner.objects.get(id=id)
    partner.delete()
    return JsonResponse({'msg': "Parceiro excluído com sucesso!", 'code': "1"})


def views_partner(request, id):
    partner = Partner.objects.get(id=id)
    context = {
        'objeto': partner
    }
    return render(request, 'partner/partner_detail.html', context)
