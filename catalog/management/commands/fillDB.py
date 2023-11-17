import json

from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        with open('category.json', encoding='utf-8') as file:
            result = json.load(file)

        category_for_create = []
        for data in result:
            category_data = {
                'id': data['pk'],
                'category_name': data['fields']['category_name'],
                'category_description': data['fields']['category_description']
            }
            category_for_create.append(Category(**category_data))
        Category.objects.bulk_create(category_for_create)

        with open('product.json', encoding='utf-8') as file:
            result = json.load(file)
        product_for_create = []
        for data in result:
            product_data = {
                'id': data['pk'],
                'product_name': data['fields']['product_name'],
                'description': data['fields']['description'],
                'category_id': data['fields']['category'],
                'price': data['fields']['price'],
            }
            product_for_create.append(Product(**product_data))
        Product.objects.bulk_create(product_for_create)
