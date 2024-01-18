from django.core.cache import cache

from catalog.models import Category, Product
from config import settings


def get_cache_categories():
    if settings.CACHE_ENABLED:
        key = 'category'
        categories = cache.get(key)
        if categories is None:
            categories = Category.objects.all()
            cache.set(key, categories)

    else:
        categories = Category.objects.all()
    return categories


def get_cache_category_detail(category_id):
    if settings.CACHE_ENABLED:
        key = 'category_detail'
        category_data = cache.get(key)
        if category_data is None:
            category_data = Product.objects.filter(category_id=category_id)
            cache.set(key, category_data)
    else:
        category_data = Product.objects.filter(category_id=category_id)
    return category_data
