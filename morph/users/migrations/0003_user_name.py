# Generated by Django 3.1.8 on 2021-04-29 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_auto_20210428_2033"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="name",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Name of User"
            ),
        ),
    ]
