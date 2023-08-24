from django.core.exceptions import ValidationError
from django.db import models


class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.IntegerField()
    date_of_applying = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    def is_adult(self) -> bool:
        return self.age >= 21

    # def save(self, *args, **kwargs) -> None:
    #     if self.age < 14:
    #         raise ValidationError("Applicants must be 14 years or older.")
    #     super().save(*args, **kwargs)

    # def clean(self) -> None:
    #     if self.age < 14:
    #         raise ValidationError("Applicants must be 14 years or older.")
    #
    # def save(self, *args, **kwargs) -> None:
    #     self.clean()
    #     super().save(*args, **kwargs)

    # class Meta:
    #     verbose_name_plural = "musicians"
