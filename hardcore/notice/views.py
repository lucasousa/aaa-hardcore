from django.shortcuts import render
from .models import Notice
from django.utils import timezone
from aaa.models import AAA
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    object_list = Notice.objects.all() #Pegando todas as notícias do banco de dados
    return render(request, 'notice/manage_notice.html', {'objetos':object_list})


def new_notice(request):
    if request.POST:
        title = request.POST['title']
        text = request.POST['content']
        athletic = AAA.objects.get(id=1)
        published_date = timezone.now()
        notice = Notice.objects.create(title = title, text = text,  published_date = published_date, athletic= athletic)
        notice.save()
        return HttpResponseRedirect(reverse('notice:index'))
    return render(request, 'notice/new_notice.html')

def edit_notice(request, id):
    if request.POST:
        title = request.POST['title']
        text = request.POST['content']
        published_date = timezone.now()
        notice = Notice.objects.get(id=id)
        notice.title = title
        notice.text = text
        notice.published_date = timezone.now()
        notice.save()
        return HttpResponseRedirect(reverse('notice:index'))
    return render(request, 'notice/edit_notice.html', {'objeto':Notice.objects.get(id=id)} )


def delete_notice(request, id):
    notice = Notice.objects.get(id=id)
    notice.delete()
    return HttpResponseRedirect(reverse('notice:index'))