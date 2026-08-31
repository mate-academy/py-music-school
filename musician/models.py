from django.core.exceptions import ValidationError
from django.db import models


class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.IntegerField()
    date_of_applying = models.DateField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def clean(self):
        if self.age < 14:
            raise ValidationError("Musician age must be at least 14")

    @property
    def is_adult(self):
        return self.age >= 21
