from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.IntegerField(
        validators=[
            MinValueValidator(15),
            MaxValueValidator(100),
        ]
    )
    date_of_applying = models.DateField(auto_now_add=True)

    @property
    def is_adult(self):
        if self.age >= 21:
            return True
        return False

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
