# Generated by Django 4.1.2 on 2023-03-13 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("locations", "0003_delete_locations_customuser_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="vehicle",
            name="is_available",
            field=models.BooleanField(default=True),
        ),
    ]