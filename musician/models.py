from django.db import models
from rest_framework.exceptions import ValidationError


class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.IntegerField()
    date_of_applying = models.DateField(auto_now_add=True)

    @property
    def is_adult(self) -> bool:
        return self.age >= 21

    def clean(self):
        if self.age is not None and self.age < 14:
            raise ValidationError({
                "age": f"Age must be at least 14 years old, not {self.age}"
            })

    def __str__(self):
        return self.first_name + " " + self.last_name
