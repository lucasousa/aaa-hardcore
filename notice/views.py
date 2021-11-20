from django.shortcuts import render
from .models import Notice
from django.utils import timezone
from aaa.models import AAA
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .forms import NoticeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import os
from django.conf import settings

@login_required
def index(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('core:my-association'))
    object_list = Notice.objects.all()
    if("busca" in request.GET):
        object_list = object_list.filter(title__icontains=request.GET["busca"])
    return render(request, 'notice/manage_notice.html', {'objetos': object_list})


@login_required
def new_notice(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('core:my-association'))
    if request.POST:
        title = request.POST['title']
        text = request.POST['text']
        image = request.FILES['featured_image']

        try:
            request.POST['is_public']
            is_public = True

        except:
            is_public = False

        athletic = AAA.objects.get(id=1)
        published_date = timezone.now()
        notice = Notice.objects.create(
            title=title, is_public=is_public, featured_image=image, text=text, published_date=published_date, athletic=athletic)
        notice.save()
        messages.success(request, 'Notícia cadastrada com sucesso.')
        return HttpResponseRedirect(reverse('notice:index'))

    notice = NoticeForm()
    return render(request, 'notice/new_notice.html', {'notice_form': notice})


@login_required
def edit_notice(request, id):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('core:my-association'))

    if request.POST:
        title = request.POST['title']
        text = request.POST['text']

        published_date = timezone.now()
        notice = Notice.objects.get(id=id)

        try:
            is_public = request.POST['is_public']
            notice.is_public = True

        except:
            notice.is_public = False

        notice.title = title
        notice.text = text
        notice.published_date = timezone.now()


        if 'featured_image' in request.FILES:
            image = request.FILES['featured_image']
            old_file = settings.MEDIA_ROOT + str(notice.featured_image)
            try:
                os.remove(old_file)
            except:
                pass
            
            notice.featured_image=image
        
        notice.save()
        messages.success(request, 'Notícia editada com sucesso.')
        return HttpResponseRedirect(reverse('notice:index'))

    instance = Notice.objects.get(id=id)
    notice = NoticeForm(instance=instance)
    return render(request, 'notice/edit_notice.html', {'objeto': instance, 'notice_form': notice})


@login_required
def delete_notice(request, id):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('core:my-association'))
    notice = Notice.objects.get(id=id)
    notice.delete()
    return JsonResponse({'msg': "Notícia excluída com sucesso!", 'code': "1"})


def notice_detail(request, slug):
    return render(request, 'notice/notice_detail.html', {'objeto': Notice.objects.get(slug=slug)})


@login_required
def copy_notice(request, id):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('core:my-association'))


    if request.method == "GET":
        notice = Notice.objects.get(id=id)
        notice.clone(id)
        messages.success(request, 'Notícia copiada com sucesso.')
        return HttpResponseRedirect(reverse('notice:index'))

    messages.error(request, 'Notícia não copiada com sucesso.')
    return HttpResponseRedirect(reverse('notice:index'))
