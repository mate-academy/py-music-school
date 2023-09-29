from django.core.exceptions import ValidationError
from django.db import models


def validate_age(age: int):
    if age < 14:
        raise ValidationError("Age should be 14 or older.")


class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.IntegerField(validators=[validate_age])
    date_of_applying = models.DateTimeField(auto_now_add=True)

    @property
    def is_adult(self) -> bool:
        return self.age > 20

    def __str__(self):
        return self.first_name + " " + self.last_name
