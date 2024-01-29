from django.db import models
from rest_framework.exceptions import ValidationError


class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.IntegerField()
    date_of_applying = models.DateField(auto_now_add=True)

    @property
    def is_adult(self):
        return self.age >= 21

    def save(self, *args, **kwargs):
        if self.age < 14:
            raise ValidationError("Age must be at least 14.")
        super(Musician, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
