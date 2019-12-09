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
from aaa.models import AAA

@login_required
def manage(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('core:my-association'))
    if not request.user.is_staff:
        return HttpResponseRedirect(reverse("core:index"))

    users = Director.objects.all().order_by('user__profile__full_name')

    if 'busca' in request.GET:
        users = users.filter(user__profile__full_name__icontains=request.GET['busca'])

    if 'message' in request.session:
        message = request.session['message']
        class_name = request.session['class']
        del request.session['message']
        del request.session['class']
        return render(request, 'director/manage.html', {'message': message, 'class': class_name, 'users': users})

    return render(request, "director/manage.html", {'users': users})

@login_required
def add(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('core:my-association'))
    if not request.user.is_staff:
        return HttpResponseRedirect(reverse("core:index"))

    if request.POST:
        try:
            user_cpf = request.POST['user'].split('| ')[1]
            user = User.objects.get(profile__cpf=user_cpf)
        except:
            request.session['message'] = 'Impossível associar este diretor. Escolha uma opção válida ao digitar o nome.'
            request.session['class'] = 'has-text-danger'
            return HttpResponseRedirect(reverse("director:manage"))
        
        user.is_superuser = True
        user.save()
        office = request.POST['office']

        aaa = AAA.objects.get(id=1)
        director = Director.objects.create(athletic=aaa, user=user, office=office)
        director.save()
        return HttpResponseRedirect(reverse("director:manage"))

    users = User.objects.all()
    
    return render(request, "director/add.html", {'users': users})

@login_required
def delete(request, id):
    if not request.user.is_staff:
        return HttpResponseRedirect(reverse("core:index"))

    director = Director.objects.get(id=id)
    user = User.objects.get(id=director.user.id)

    if not user.is_staff:
        user.is_superuser = False
        user.save()
    
    director.delete()

    return HttpResponseRedirect(reverse("director:manage"))
