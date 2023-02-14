from django.core.validators import MinValueValidator
from django.db import models


class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.IntegerField(
        validators=[
            MinValueValidator(
                limit_value=14, message="Students must be 14 years old or above"
            )
        ]
    )
    date_of_applying = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def is_adult(self):
        return self.age >= 21
