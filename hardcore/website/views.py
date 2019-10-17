from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'website/index.html')

def login(request):
    return render(request, 'website/login.html')