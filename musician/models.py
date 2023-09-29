from django.db import models
from django.core.validators import MinValueValidator


class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.PositiveIntegerField(validators=(MinValueValidator(14),))
    date_of_applying = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name

    @property
    def is_adult(self):
        return True if self.age >= 21 else False
