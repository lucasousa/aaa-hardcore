from django.shortcuts import render
from .models import Partner
from django.http import HttpResponseRedirect
from django.urls import reverse
import os
from django.conf import settings
 

# Create your views here.

def index(request):
    object_list = Partner.objects.all()
    if("busca" in request.GET):
        object_list = object_list.filter(name__icontains=request.GET["busca"])
    return render(request, 'partner/manage-partner.html', {'objetos':object_list})

def add(request):
    if request.POST:
        logo = request.FILES['logo']
        description = request.POST['description']
        name = request.POST['name']
        partner = Partner.objects.create(name = name, logo = logo, description = description)
        partner.save()
        return HttpResponseRedirect(reverse('partner:index'))
    return render(request, 'partner/add.html')

def edit(request, id):
    if request.POST:
        description = request.POST['description']
        name = request.POST['name']
        partner = Partner.objects.get(id=id)
        partner.name = name
        partner.description = description
        if 'logo' in request.FILES:
            logo = request.FILES['logo']
            old_file = settings.MEDIA_ROOT + str(partner.logo)
            try:
                os.remove(old_file)
            except:
                pass

            partner.logo = logo

        partner.save()
        return HttpResponseRedirect(reverse('partner:index'))
    return render(request, 'partner/edit.html', {'objeto':Partner.objects.get(id=id)} )

def deletar(request, id):
    partner = Partner.objects.get(id=id)
    partner.delete()
    return HttpResponseRedirect(reverse('partner:index'))

def views_partner(request,id):
    partner = Partner.objects.get(id=id)
    res = {
        'objeto':partner
    }
    return render(request,'partner/partner_detail.html',res)