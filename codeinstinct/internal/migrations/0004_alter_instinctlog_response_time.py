# Generated by Django 4.2.2 on 2023-07-22 09:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("internal", "0003_alter_instinctlog_table"),
    ]

    operations = [
        migrations.AlterField(
            model_name="instinctlog",
            name="response_time",
            field=models.DecimalField(
                blank=True, decimal_places=4, max_digits=4, null=True
            ),
        ),
    ]