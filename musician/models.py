from django.db import models
from django.core.validators import MinValueValidator
from .constants import MAX_LENGTH, MIN_AGE, ADULT_AGE


class Musician(models.Model):
    first_name = models.CharField(
        max_length=MAX_LENGTH,
        help_text="First name of the musician"
    )
    last_name = models.CharField(
        max_length=MAX_LENGTH,
        help_text="Last name of the musician"
    )
    instrument = models.CharField(
        max_length=MAX_LENGTH,
        help_text="Instrument played by the musician"
    )
    age = models.IntegerField(
        validators=[MinValueValidator(MIN_AGE)],
        help_text=f"Age of the musician (minimum {MIN_AGE} years)"
    )
    date_of_applying = models.DateField(
        auto_now_add=True,
        help_text="Date when the musician applied"
    )

    def __str__(self):
        """String representation of the Musician object."""
        return f"{self.first_name} {self.last_name}"

    @property
    def is_adult(self) -> bool:
        """Check if the musician is an adult."""
        return self.age >= ADULT_AGE
