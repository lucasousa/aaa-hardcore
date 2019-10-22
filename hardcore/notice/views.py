from django.shortcuts import render
from .models import Notice
from django.utils import timezone
from aaa.models import AAA

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
    return render(request, 'notice/new_notice.html')
