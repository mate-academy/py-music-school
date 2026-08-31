from rest_framework import serializers

from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        is_adult = serializers.IntegerField(source="is_adult")
        capacity = serializers.IntegerField(source="cinema_hall.capacity")
        fields = (
            "id",
            "first_name",
            "last_name",
            "instrument",
            "age",
            "is_adult",
        )
