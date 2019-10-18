from django.contrib import admin
from notice.models import Notice


class NoticeAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'published_date']
    actions = []

admin.site.register(Notice)