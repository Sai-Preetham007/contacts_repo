# Generated by Django 5.1.1 on 2024-10-11 01:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contacts_app", "0003_user_contacts_alter_user_mobile_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="user_contacts",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="contacts",
                to="contacts_app.user",
            ),
        ),
    ]
