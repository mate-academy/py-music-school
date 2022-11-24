from django.core.exceptions import BadRequest

from django.db import models


class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.IntegerField()
    date_of_applying = models.DateField(auto_now_add=True)

    @property
    def is_adult(self):
        return self.age >= 21

    def clean(self):
        if not (self.age >= 14):
            raise BadRequest({
                "age": f"age must be >= 14, not {self.age}"
            })

    def save(
        self, force_insert=False, force_update=False,
            using=None, update_fields=None
    ):
        self.full_clean()
        return super(Musician, self).save(
            force_insert, force_update, using, update_fields
        )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
