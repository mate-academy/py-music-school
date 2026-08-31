from rest_framework import serializers
from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer[Musician]):
    class Meta:
        model = Musician
        fields = (
            "id",
            "first_name",
            "last_name",
            "instrument",
            "age",
            "is_adult",
            "date_of_applying"
        )
        read_only_fields = ("date_of_applying", "id")
