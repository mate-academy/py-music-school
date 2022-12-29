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

    def __str__(self):
        return self.first_name + " " + self.last_name

    def clean(self):
        if self.age < 14:
            raise ValueError({
                "age": f"age must be more or equal than 14 "
            })

    # def save(
    #     self,
    #     force_insert=False,
    #     force_update=False,
    #     using=None,
    #     update_fields=None
    # ):
    #     self.full_clean()
    #     return super(Musician, self).save(
    #         force_insert,
    #         force_update,
    #         using,
    #         update_fields
    #     )
