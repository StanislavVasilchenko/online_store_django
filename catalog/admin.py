from django.contrib import admin

from catalog.models import Product, Category, Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('product_name', 'description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'category_description')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'number', 'is_activ',)

