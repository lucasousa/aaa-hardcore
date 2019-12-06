from django.urls import path
from . import views

app_name = 'director'

urlpatterns = [
    path('', views.manage, name="manage"),
    path('add/', views.add, name="add"),
]