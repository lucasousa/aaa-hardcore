from django.urls import path
from . import views


app_name = 'notice'

urlpatterns = [
    path('', views.index, name='index'),
    path('new_notice/', views.new_notice, name='new_notice')
]