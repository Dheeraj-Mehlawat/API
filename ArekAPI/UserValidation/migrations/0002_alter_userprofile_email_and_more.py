# Generated by Django 4.2 on 2024-04-10 07:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("UserValidation", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="phone_number",
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
