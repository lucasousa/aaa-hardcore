import datetime

from aaa.models import AAA
from core.models import Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from .models import Association


@login_required
def index(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse("core:my-association"))
    object_list = User.objects.all()

    if "filter" in request.GET and request.GET["filter"] == "not-associated":
        object_list = [x for x in object_list if not x.profile.has_associated]

    if "busca" in request.GET:
        object_list = object_list.filter(
            profile__full_name__icontains=request.GET["busca"]
        )
    return render(
        request, "association/manage-association.html", {"objetos": object_list}
    )


@login_required
def add(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse("core:my-association"))
    usuario = User.objects.get(id=request.GET["data"])
    atletica = AAA.objects.get(id=1)
    expiration_date = datetime.date.today().replace(year=datetime.date.today().year + 1)
    association = Association.objects.create(
        expiration_date=expiration_date, user=usuario, athletic=atletica
    )
    association.save()
    messages.success(request, "Associação realizada com sucesso!")
    return JsonResponse({"mensagem": "Associação criada com sucesso!", "code": "1"})


@login_required
def deletar(request, id):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse("core:my-association"))

    user = User.objects.get(id=id)
    association = Association.objects.get(user=user)
    association.delete()
    return HttpResponseRedirect(reverse("association:index"))


@login_required
def edit(request, id):

    user = User.objects.get(id=id)
    profile = Profile.objects.get(user=user)
    if request.method == "POST":
        formData = request.POST
        profile.full_name = formData["name"]
        profile.user.email = formData["email"]
        profile.course_name = formData["course"]
        profile.date_birth = formData["birth-date"]
        profile.sex = formData["sex"]
        profile.save()
        messages.success(request, "Informações alteradas com sucesso!")
        return HttpResponseRedirect(reverse("core:my-association"))

    return render(request, "association/edit-association.html", {"objeto": profile})

    """
        description = request.POST['description']
        name = request.POST['name']
        partner = Partner.objects.get(id=id)
        partner.name = name
        partner.description = description
        if 'logo' in request.FILES:
            logo = request.FILES['logo']
            old_file = settings.MEDIA_ROOT + str(partner.logo)
            try:
                os.remove(old_file)
            except:
                pass

            partner.logo = logo
    """
    return JsonResponse({"msg": "Associação excluída com sucesso!", "code": "1"})


@login_required
def student_infos(request, id):
    user = User.objects.get(id=id)
    return render(request, "association/student_details.html", {"object": user})
