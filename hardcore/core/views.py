from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse
import random
from association.models import Association

# Create your views here.
@login_required
def index(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('core:my-association'))

    return render(request, "core/index.html")

@login_required
@require_POST
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('website:index'))

@login_required
def my_association(request):
    try:
        association = Association.objects.get(user=request.user) 
    except:
        association = None

    return render(request, "core/my-association.html", {'association': association})
