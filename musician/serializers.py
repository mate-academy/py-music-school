from rest_framework import serializers

from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = (
            "first_name",
            "last_name",
            "instrument",
            "age",
            "date_of_applying",
            "is_adult"
        )

    def validate(self, attrs):
        if attrs["age"] <= 14:
            raise serializers.ValidationError(
                "You are too young to be accepted in our school"
            )
        return attrs
