from rest_framework import serializers

from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = (
            "id",
            "first_name",
            "last_name",
            "age",
            "instrument",
            "date_of_applying",
            "is_adult",
        )
