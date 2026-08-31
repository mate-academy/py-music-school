from rest_framework import serializers
from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = (
            "is_adult",
            "first_name",
            "last_name",
            "instrument",
            "age",
            "date_of_applying"
        )
