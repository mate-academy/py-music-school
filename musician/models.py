from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.IntegerField(
        validators=[
            MinValueValidator(
                14, message="We do not accept people who are under 14!"
            ),
            MaxValueValidator(
                70,
                message="Age cannot be more than 70!(age discrimination)"
            )
        ]
    )
    date_of_applying = models.DateField(auto_now_add=True)

    @property
    def is_adult(self):
        return self.age >= 21

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
