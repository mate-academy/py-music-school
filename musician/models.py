from django.db import models


class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(
        max_length=63,
        help_text="Type of instrument played"
    )
    age = models.IntegerField()
    date_of_applying = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def is_adult(self):
        return self.age >= 21

    def save(self, *args, **kwargs):
        from rest_framework.exceptions import ValidationError

        if self.age < 14:
            raise ValidationError({
                "age": (
                    "Musicians must be at least 14 years old."
                )
            })
        super().save(*args, **kwargs)
