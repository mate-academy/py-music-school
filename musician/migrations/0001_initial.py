# Generated by Django 4.1 on 2022-11-20 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=63)),
                ('last_name', models.CharField(max_length=63)),
                ('instrument', models.CharField(max_length=63)),
                ('age', models.IntegerField()),
                ('date_of_applying', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
