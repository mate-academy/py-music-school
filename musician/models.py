from django.db import models
from django.core import validators

class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.IntegerField(validators=[validators.MinValueValidator(14)])
    date_of_applying = models.DateTimeField(auto_now_add=True)

    @property
    def is_adult(self) -> bool:
        return True if self.age > 20 else False

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
