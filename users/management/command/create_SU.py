from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        users = User.objects.create(
            email='stanislav.vasilchenko@yandex.ru',
            first_name='stanislav',
            last_name='vasilchenko',
            is_staff=True,
            is_superuser=True,
        )
        users.set_password('admin')
        users.save()