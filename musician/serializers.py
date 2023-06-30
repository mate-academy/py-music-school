from rest_framework import serializers

from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    is_adult = serializers.ReadOnlyField()

    class Meta:
        model = Musician
        fields = (
            "first_name",
            "last_name",
            "instrument",
            "age",
            "date_of_applying",
            "is_adult"
        )
