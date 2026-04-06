from django.db import models
from django.core.validators import MinValueValidator


class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.IntegerField(validators=[MinValueValidator(15)])
    date_of_applying = models.DateField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    @property
    def is_adult(self):
        return self.age >= 21
