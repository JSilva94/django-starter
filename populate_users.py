import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'protwo.settings')

import django
django.setup()

from faker import Faker

from app_two.models import User

fakegen = Faker()


def populate(n):
    for _ in range(n):
        fake_first_name = fakegen.name()
        fake_last_name = fakegen.name()
        fake_email = fakegen.email()

        users = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email: fake_email)[0]


if '__name__' == '__main__':
    print('populating users')
    populate(5)
    print('populating complete')
