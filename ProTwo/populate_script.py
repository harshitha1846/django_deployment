import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

from AppTwo.models import User
from faker import Faker

fake_data = Faker()

def populate(N=7):
    for _ in range(N):
        fake_firstName = fake_data.first_name()
        fake_lastName = fake_data.last_name()
        fake_email = fake_data.email()

        user = User(FirstName=fake_firstName, LastName=fake_lastName, Email=fake_email)
        user.save()

if __name__ == '__main__':
    print('populating script')
    populate(20)
    print('populating complete')
