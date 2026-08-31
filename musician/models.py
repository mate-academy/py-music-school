from django.db import models
from rest_framework.exceptions import ValidationError


def age_validator(value):
    if value < 14:
        raise ValidationError(f"age must be over 13 years old, not {value}")


class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.PositiveIntegerField(validators=[age_validator])
    date_of_applying = models.DateTimeField(auto_now_add=True)

    def is_adult(self):
        return self.age >= 21

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
