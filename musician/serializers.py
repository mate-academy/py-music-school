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

    @staticmethod
    def validate_age(value):
        if value < 14:
            raise serializers.ValidationError("need to old man")
        return value
