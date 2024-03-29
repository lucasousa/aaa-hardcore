from django.urls import path
from . import views

app_name = 'partner'

urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.add, name="add"),
    path('edit/<int:id>',views.edit, name="edit"),
    path('deletar/<int:id>',views.deletar, name="deletar"),
    path('views_partner/<int:id>', views.views_partner, name='views_partner'),
]
