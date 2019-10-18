from django.shortcuts import render
from .models import Partner

# Create your views here.

def index(request):
    object_list = Partner.objects.all()
    return render(request, 'partner/manage-partner.html', {'objetos':object_list})

def add(request):
    return render(request, 'partner/add.html')