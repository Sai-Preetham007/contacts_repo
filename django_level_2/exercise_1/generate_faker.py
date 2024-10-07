import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "exercise_1.settings")

import django
django.setup()

import random
from faker import Faker
from exercise_app.models import users

def populate(N=5):
    for i in range(N):
        fake_name = Faker().name().split()
        first_name = fake_name[0]
        last_name = fake_name[1]
        fake_email = Faker().email()
        user = users.objects.get_or_create(first_name = first_name, last_name = last_name, email = fake_email)


if __name__=="__main__":
    print("Populating the fake data.")
    populate(25)
    print("Completed")