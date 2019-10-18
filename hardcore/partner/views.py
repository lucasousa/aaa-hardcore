from django.shortcuts import render
from .models import Partner

# Create your views here.

def index(request):
    object_list = Partner.objects.all()
    return render(request, 'partner/manage-partner.html', {'objetos':object_list})

def add(request):
    if request.POST:
        logo = request.FILES['logo']
        description = request.POST['description']
        name = request.POST['name']
        partner = Partner.objects.create(name = name, logo = logo, description = description)
        partner.save()
    return render(request, 'partner/add.html')