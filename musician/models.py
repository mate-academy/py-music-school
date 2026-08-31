from typing import Any

from django.db import models
from rest_framework.exceptions import ValidationError


class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.IntegerField()
    date_of_applying = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    @property
    def is_adult(self):
        return self.age >= 21

    def clean(self) -> None:
        age = self.age
        if age < 14:
            raise ValidationError(
                {
                    "age": [
                        (
                            "We do not accept people who are under 14: "
                            f"Your age is {age})"
                        )
                    ]
                }
            )

    def save(
            self,
            force_insert: bool = False,
            force_update: bool = False,
            using: Any = None,
            update_fields: Any = None
    ) -> super:
        self.full_clean()
        return super(Musician, self).save(
            force_insert,
            force_update,
            using,
            update_fields
        )
