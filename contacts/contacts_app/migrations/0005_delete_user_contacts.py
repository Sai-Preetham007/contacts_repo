# Generated by Django 5.1.1 on 2024-10-12 22:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("contacts_app", "0004_user_contacts_user"),
    ]

    operations = [
        migrations.DeleteModel(
            name="User_contacts",
        ),
    ]
