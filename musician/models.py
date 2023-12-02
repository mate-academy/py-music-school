from django.db import models
from django.core.exceptions import ValidationError


class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.IntegerField()
    date_of_applying = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ("age",)

    @property
    def is_adult(self) -> bool:
        return self.age >= 21

    def clean(self) -> None:
        if self.age and self.age < 14:
            raise ValidationError(
                {"age": "We do not accept people who are under 14"}
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
