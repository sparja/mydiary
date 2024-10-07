from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    '''Создание суперпользователя'''

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@admin.com',
            first_name='admin',
            last_name='admin',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('449558')
        user.save()
