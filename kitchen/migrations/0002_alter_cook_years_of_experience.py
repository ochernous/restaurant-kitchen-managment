# Generated by Django 4.2.5 on 2023-10-01 21:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kitchen", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cook",
            name="years_of_experience",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
