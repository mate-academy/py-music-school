from rest_framework import serializers
from .models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    is_adult = serializers.ReadOnlyField()

    class Meta:
        model = Musician
        fields = [
            "id",
            "first_name",
            "last_name",
            "instrument",
            "age",
            "date_of_applying",
            "is_adult"
        ]

    def validate_age(self, value):
        if value < 14:
            raise serializers.ValidationError(
                "Musicians must be at least 14 years old."
            )
        return value
