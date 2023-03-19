from django.core.exceptions import ValidationError
from django.db import models


class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.IntegerField()
    date_of_applying = models.DateField(auto_now_add=True)

    @property
    def is_adult(self):
        return self.age >= 21

    def clean(self):
        if not self.age > 14:
            raise ValidationError(
                {
                    "age": "You are too young to be accepted in our school"
                }
            )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
