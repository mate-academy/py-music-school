from rest_framework import serializers

from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        read_only_fields = ["is_adult"]
        fields = [
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
                "You must be at least 14 years old."
            )
        return value
