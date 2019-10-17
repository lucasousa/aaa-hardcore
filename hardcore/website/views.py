from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request, 'website/index.html')

def login_user(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/core/")

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
        
    if 'mensagem' in request.session:
        mensagem = request.session['mensagem']
        classe = request.session['classe']
        del request.session['mensagem']
        del request.session['classe']
        return render(request, 'website/login.html', {'message': mensagem, 'class': classe})

    return render(request, 'website/login.html')
