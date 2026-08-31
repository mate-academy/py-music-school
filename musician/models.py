from django.db import models
from rest_framework.exceptions import ValidationError


class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.IntegerField()
    date_of_applying = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    def is_adult(self) -> int:
        return self.age >= 21

    def clean(self) -> None:
        if self.age < 14:
            raise ValidationError("Age should be more than 14 years")

    def save(
            self,
            force_insert=False,
            force_update=False,
            using=None,
            update_fields=None,
    ) -> None:
        self.full_clean()
        super(Musician, self).save(
            force_insert, force_update, using, update_fields
        )
