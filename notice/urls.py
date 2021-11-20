from django.urls import path
from . import views


app_name = 'notice'

urlpatterns = [
    path('', views.index, name='index'),
    path('new_notice/', views.new_notice, name='new_notice'),
    path('edit_notice/<int:id>', views.edit_notice, name="edit_notice"),
    path('delete_notice/<int:id>', views.delete_notice, name="delete_notice"),
    path('detail_notice/<slug:slug>', views.notice_detail, name="detail_notice"),
    path('copy_notice/<int:id>', views.copy_notice, name="copy_notice")
]