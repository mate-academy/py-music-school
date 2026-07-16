from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from musician.models import Musician


class MusicianSerializer(ModelSerializer):
    age = serializers.IntegerField(min_value=21)
    is_adult = serializers.BooleanField(read_only=True)

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
