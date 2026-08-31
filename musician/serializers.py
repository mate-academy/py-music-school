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
            "is_adult",
            "instrument",
            "date_of_applying"
        )
