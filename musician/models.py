from django.core.exceptions import ValidationError
from django.db import models


def validate_age(value):
    if value <= 14:
        raise ValidationError("Age must be over 14.")


class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.IntegerField(validators=[validate_age])
    date_of_applying = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    def is_adult(self):
        return self.age >= 21
