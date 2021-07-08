from django.contrib import admin
from product.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'value', 'image']
    actions = []

admin.site.register(Product)
