from django.db import models
from rest_framework.exceptions import ValidationError


def validate_minimal_years(value):
    if value < 14:
        raise ValidationError(
            "You are so young, come when you`re 14"
        )


class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.IntegerField(validators=[validate_minimal_years])
    date_of_applying = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def is_adult(self):
        if self.age >= 21:
            return True
        return False
