from django.shortcuts import render
from .models import Notice
from django.utils import timezone
from aaa.models import AAA
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import NoticeForm

def index(request):
    object_list = Notice.objects.all() #Pegando todas as notícias do banco de dados
    if("busca" in request.GET):
        object_list = object_list.filter(title__icontains=request.GET["busca"])
    return render(request, 'notice/manage_notice.html', {'objetos':object_list})

def new_notice(request):
    if request.POST:
        title = request.POST['title']
        text = request.POST['text']
        athletic = AAA.objects.get(id=1)
        published_date = timezone.now()
        notice = Notice.objects.create(title = title, text = text,  published_date = published_date, athletic= athletic)
        notice.save()
        return HttpResponseRedirect(reverse('notice:index'))

    notice = NoticeForm()
    return render(request, 'notice/new_notice.html', {'notice_form': notice})

def edit_notice(request, id):
    if request.POST:
        title = request.POST['title']
        text = request.POST['text']
        published_date = timezone.now()
        notice = Notice.objects.get(id=id)
        notice.title = title
        notice.text = text
        notice.published_date = timezone.now()
        notice.save()
        return HttpResponseRedirect(reverse('notice:index'))

    instance = Notice.objects.get(id=id)
    notice = NoticeForm(instance=instance)
    return render(request, 'notice/edit_notice.html', {'objeto':instance, 'notice_form': notice} )


def delete_notice(request, id):
    notice = Notice.objects.get(id=id)
    notice.delete()
    return HttpResponseRedirect(reverse('notice:index'))

def notice_detail(request, slug):
    return render(request, 'notice/notice_detail.html', {'objeto':Notice.objects.get(slug=slug)})