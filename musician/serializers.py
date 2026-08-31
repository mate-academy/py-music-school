from rest_framework import serializers

from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):
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

    def validate_age(self, value):
        if value < 14:
            raise serializers.ValidationError(
                "We do not accept people who are under 14"
            )
        return value
