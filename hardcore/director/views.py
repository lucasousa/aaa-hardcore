from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse
import random
from association.models import Association
from .models import Director

@login_required
def manage(request):
    if not request.user.is_staff:
        return HttpResponseRedirect(reverse("core:index"))
    
    users = Director.objects.all().order_by('user__profile__full_name')
    return render(request, "director/manage.html", {'users': users})

@login_required
def add(request):
    if not request.user.is_staff:
        return HttpResponseRedirect(reverse("core:index"))
    
    return render(request, "director/add.html")
