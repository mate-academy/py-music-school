from django.core.exceptions import ValidationError
from django.db import models


class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.IntegerField()
    date_of_applying = models.DateTimeField(auto_now_add=True)

    @property
    def is_adult(self):
        return self.age >= 21

    @staticmethod
    def validate_age(age: int, error_to_raise):
        if age < 14:
            raise error_to_raise({
                "age": "Musicians under the age of 14 are not accepted."
            })

    def clean(self):
        Musician.validate_age(self.age, ValidationError)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
