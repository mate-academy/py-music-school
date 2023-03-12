from django.core.validators import MinValueValidator
from django.db import models


class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.IntegerField(
        validators=[MinValueValidator(
            14, message="We do not accept people who are under 14"
        )]
    )
    date_of_applying = models.DateTimeField(auto_now_add=True)

    @property
    def is_adult(self) -> bool:
        if self.age >= 21:
            return True
        return False

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
