from django.db import models
from rest_framework.exceptions import ValidationError


class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.PositiveIntegerField()
    date_of_applying = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "musicians"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def clean(self):
        if self.age < 14:
            raise ValidationError("Musicians must be at least 14 years old.")

    @property
    def is_adult(self):
        return self.age >= 21

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
