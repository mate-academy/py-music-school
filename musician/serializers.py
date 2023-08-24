from rest_framework import serializers

from .models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    is_adult = serializers.BooleanField(read_only=True)

    class Meta:
        model = Musician
        fields = (
            "id",
            "first_name",
            "last_name",
            "instrument",
            "age",
            "date_of_applying",
            "is_adult",
        )

    @staticmethod
    def validate_age(value: int) -> int:
        if value < 14:
            raise serializers.ValidationError(
                "Applicants must be 14 years or older."
            )
        return value
