from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse
import random


# Create your views here.
def index(request):
    return render(request, 'website/index.html')

def login_user(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('core:index'))

    if 'next' in request.GET:
        request.session['redirect'] = request.GET['next']
    
    if request.POST:
        email = request.POST['email']
        email = email.lower()
        senha = request.POST['password']
        try:
            user = User.objects.get(email=email)
            if user:
                user = authenticate(request, username=user.username, password=senha)
                if user is not None:
                    login(request, user)
                    if 'redirect' in request.session:
                        redirect = request.session['redirect']
                        del request.session['redirect']
                        return HttpResponseRedirect(redirect)

                    return HttpResponseRedirect(reverse('core:index'))
                else:
                    return render(request, 'website/login.html', {'message': 'E-mail ou senha incorretos.', 'class': 'has-text-danger'})    

        except User.DoesNotExist:
            return render(request, 'website/login.html', {'message': 'E-mail ou senha incorretos.', 'class': 'has-text-danger'})    
        
    if 'message' in request.session:
        message = request.session['message']
        class_name = request.session['class']
        del request.session['message']
        del request.session['class']
        return render(request, 'website/login.html', {'message': message, 'class': class_name})

    return render(request, 'website/login.html')

def signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('core:index'))

    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        course = request.POST['course']
        cpf = request.POST['cpf']
        birth_date = request.POST['birth-date']
        sex = request.POST['sex']

        choices = 'qwertyuiopasdfghjklzxcvbnm1234567890' 
        username = ''
        for i in range(18):
            username += random.choice(choices)
        
        while User.objects.filter(username=username).exists():
            username = ''
            for i in range(18):
                username += random.choice(choices)

        if User.objects.filter(email=email).exists():
            return render(request, 'website/signup.html', {'message': 'E-mail já cadastrado.', 'class': 'has-text-danger'})

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        user.profile.full_name = name
        user.profile.course_name = course
        user.profile.cpf = cpf
        user.profile.birth_date = birth_date
        user.profile.sex = sex
        user.save()

        request.session['message'] = 'Usuário cadastrado com sucesso. Faça Login'
        request.session['class'] = 'has-text-success'

        return HttpResponseRedirect(reverse('website:login'))
    
    return render(request, 'website/signup.html')
