import random

from core.validators import validate_cpf
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from notice.models import Notice
from partner.models import Partner
from product.models import Product


# Create your views here.
def index(request):
    product = Product.objects.all().order_by("-id")[:4]
    partner = Partner.objects.all().order_by("-id")[:4]
    notice = Notice.objects.all().order_by("-published_date").filter(is_public=True)[:4]
    res = {
        "objeto": product,
        "notice": notice,
        "partner": partner,
    }
    return render(request, "website/index.html", res)


def login_user(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("core:index"))

    if "next" in request.GET:
        request.session["redirect"] = request.GET["next"]

    if request.POST:
        email = request.POST["email"]
        email = email.lower()
        senha = request.POST["password"]
        try:
            user = User.objects.get(Q(email=email) | Q(username=email))
            if user:
                user = authenticate(request, username=user.username, password=senha)
                if user is not None:
                    login(request, user)
                    if "redirect" in request.session:
                        redirect = request.session["redirect"]
                        del request.session["redirect"]
                        return HttpResponseRedirect(redirect)

                    return HttpResponseRedirect(reverse("core:index"))
                else:
                    return render(
                        request,
                        "website/login.html",
                        {
                            "message": "E-mail ou senha incorretos.",
                            "class": "has-text-danger",
                        },
                    )

        except User.DoesNotExist:
            return render(
                request,
                "website/login.html",
                {"message": "E-mail ou senha incorretos.", "class": "has-text-danger"},
            )

    if "message" in request.session:
        message = request.session["message"]
        class_name = request.session["class"]
        del request.session["message"]
        del request.session["class"]
        return render(
            request, "website/login.html", {"message": message, "class": class_name}
        )

    return render(request, "website/login.html")


def signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("core:index"))

    if request.POST:
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        course = request.POST["course"]
        cpf = request.POST["cpf"]
        birth_date = request.POST["birth-date"]
        sex = request.POST["sex"]

        choices = "qwertyuiopasdfghjklzxcvbnm1234567890"
        username = ""
        for i in range(18):
            username += random.choice(choices)

        while User.objects.filter(username=username).exists():
            username = ""
            for i in range(18):
                username += random.choice(choices)

        if User.objects.filter(email=email).exists():
            return render(
                request,
                "website/signup.html",
                {"message": "E-mail já cadastrado.", "class": "has-text-danger"},
            )

        try:
            validate_cpf(cpf)
        except ValidationError:
            context = {"message": "Esse CPF é inválido.", "class": "has-text-danger"}
            return render(request, "website/signup.html", context)

        user = User.objects.create_user(
            username=username, email=email, password=password
        )
        user.save()
        user.profile.full_name = name
        user.profile.course_name = course
        user.profile.cpf = cpf
        user.profile.birth_date = birth_date
        user.profile.sex = sex
        user.save()

        request.session["message"] = "Usuário cadastrado com sucesso. Faça Login"
        request.session["class"] = "has-text-success"

        return HttpResponseRedirect(reverse("website:login"))

    return render(request, "website/signup.html")


def product_list(request):
    object_list = Product.objects.all()
    res = {
        "objeto": object_list,
    }
    return render(request, "website/list-product.html", res)


def notice_list(request):
    object_list = Notice.objects.all().order_by("-published_date").filter(is_public=True)
    res = {
        "notice": object_list,
    }
    return render(request, "website/list-notice.html", res)


def partner_list(request):
    object_list = Partner.objects.all().order_by("-id")
    res = {
        "partner": object_list,
    }
    return render(request, "website/list-partner.html", res)


def about(request):
    return render(request, "website/about.html")


def contact(request):
    return render(request, "website/contact.html")
