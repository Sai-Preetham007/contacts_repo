import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "second_project.settings")

import django
django.setup()

import random
from faker import Faker
from second_app.models import Topic, Webpage, AccessRecord

topics = ["Social", "News", "Sports", "Market", "Search"]



def add_topic():
    t = Topic.objects.get_or_create(topic_name = random.choice(topics))[0]
    t.save()
    return t



def populate(N = 5):
    for i in range(N):
        top = add_topic()
        fake_name = Faker().company()
        fake_url = Faker().url()
        fake_date = Faker().date()
        webpg = Webpage.objects.get_or_create(topic = top, name = fake_name, url = fake_url)[0]
        acc_rec = AccessRecord.objects.get_or_create(name = webpg, date = fake_date)[0]



if __name__ == "__main__":
    print("Populating Fake Script.......")
    populate(10)
    print("Populating Complete....")