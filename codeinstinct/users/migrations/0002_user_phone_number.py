# Generated by Django 4.2.2 on 2023-07-22 08:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="phone_number",
            field=models.CharField(max_length=12, null=True),
        ),
    ]
