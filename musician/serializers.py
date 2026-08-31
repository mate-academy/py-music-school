from musician.models import Musician
from rest_framework import serializers


class MusicianSerializer(serializers.ModelSerializer):
    is_adult = serializers.ReadOnlyField()

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
