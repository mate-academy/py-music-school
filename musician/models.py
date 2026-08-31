from importlib.metadata import requires

from django.db import models
from django.core.exceptions import ValidationError
from rest_framework.exceptions import ParseError


class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.IntegerField()
    date_of_applying = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def is_adult(self):
        if self.age >= 21:
            return "Person is adult"
        else:
            return "Person is not adult"

    class Meta:
        verbose_name = "Musician"
