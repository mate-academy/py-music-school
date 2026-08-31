from django.db import models


def validate_age(age: int):
    if age < 14:
        raise ValueError("We do not accept people who under 14")


class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.IntegerField(validators=[validate_age])
    date_of_applying = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    def is_adult(self) -> bool:
        return self.age >= 21
