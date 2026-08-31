from typing import Type

from django.db import models
from django.core.exceptions import ValidationError


class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.IntegerField()
    date_of_applying = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    def is_adult(self) -> bool:
        return 21 >= self.age

    def age_clean(self) -> None:
        if self.age < 14:
            raise ValidationError("We do not accept people who are under 14")

    def save(self, *args, **kwargs) -> Type["Musician"]:
        self.full_clean()
        return super().save(*args, **kwargs)
