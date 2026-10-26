from rest_framework import serializers

from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    date_of_applying = serializers.DateField(
        read_only=True, required=False
    )
    is_adult = serializers.BooleanField(
        read_only=True, required=False
    )

    class Meta:
        model = Musician
        fields = (
            "id",
            "first_name",
            "last_name",
            "instrument",
            "age",
            "date_of_applying",
            "is_adult"
        )
