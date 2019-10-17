from django.urls import path
from . import views

app_name = 'partner'

urlpatterns = [
    path('', views.index, name="index"),
]
