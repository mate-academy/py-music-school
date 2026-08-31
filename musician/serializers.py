from django.core.validators import MinValueValidator
from rest_framework import serializers

from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField(
        validators=[MinValueValidator(14)]
    )

    class Meta:
        model = Musician
        fields = ("first_name",
                  "last_name",
                  "age",
                  "instrument",
                  "is_adult",
                  "date_of_applying"
                  )
        read_only_fields = ("is_adult", "date_of_applying")
