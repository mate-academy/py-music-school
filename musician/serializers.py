from rest_framework import serializers

from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source="__str__", read_only=True)

    class Meta:
        model = Musician
        fields = (
            "first_name",
            "last_name",
            "full_name",
            "instrument",
            "age",
            "date_of_applying",
            "is_adult"
        )
        read_only_fields = ("id", "date_of_applying", "is_adult")

    @staticmethod
    def validate_age(value):
        if value is not None and value < 14:
            raise serializers.ValidationError(
                "We do not accept people who are under 14"
            )
        return value
