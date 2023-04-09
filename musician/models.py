from __future__ import annotations

from django.db import models
from rest_framework.exceptions import ValidationError


class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.IntegerField()
    date_of_applying = models.DateField(auto_now_add=True)

    @property
    def is_adult(self) -> bool:
        return self.age >= 21

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def clean(self) -> None:
        if not self.age >= 14:
            raise ValidationError({
                "age": "Musician must be under 13 y.o."
            })

    def save(
            self,
            force_insert=False,
            force_update=False,
            using=None,
            update_fields=None
    ) -> Musician:
        self.full_clean()
        return super(Musician, self).save(
            force_insert,
            force_update,
            using,
            update_fields
        )
