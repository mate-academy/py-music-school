from django.db import models
from rest_framework.exceptions import ValidationError


class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.IntegerField()
    date_of_applying = models.DateField(auto_now_add=True)

    @staticmethod
    def validate_age(age: int, valid_age: int, error_to_raise):
        if not (age >= valid_age):
            raise error_to_raise({
                "age": f"age should be bigger than {valid_age}"
            })

    def clean(self):
        Musician.validate_age(self.age, 14, ValidationError)

    @property
    def is_adult(self):
        return True if self.age >= 21 else False

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
