# Generated by Django 4.1 on 2023-07-31 12:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musician', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(14)]),
        ),
    ]
