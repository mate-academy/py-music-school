# Generated by Django 4.1 on 2023-03-31 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("musician", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="musician",
            options={"verbose_name_plural": "musicians"},
        ),
    ]
