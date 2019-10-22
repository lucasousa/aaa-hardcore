from django.urls import path, include
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name="index"),
    path('logout/', views.logout_user, name="logout_user"),
]
