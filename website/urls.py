from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login_user, name="login"),
    path('signup/', views.signup, name="signup"),
    path('produtos/', views.product_list, name="product_list"),
    path('noticias/', views.notice_list, name="notice_list"),
    path('parceiros/', views.partner_list, name="partner_list"),
    path('about/', views.about, name="about"),
    path('contato/', views.contact, name="contact"),
]
