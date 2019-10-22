from django.shortcuts import render
from .models import Notice

def index(request):
    object_list = Notice.objects.all() #Pegando todas as notícias do banco de dados
    return render(request, 'notice/manage_notice.html', {'objetos':object_list})


def new_notice(request):
    if request.POST:
        title = request.POST['title']
        text = request.POST['text']
        post.published_date = timezone.now()
        notice = Notice.objects.create(title = title, text = text,  published_date = post.published_date)
        notice.save()
    return render(request, 'notice/new_notice.html')
