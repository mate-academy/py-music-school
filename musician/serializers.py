from rest_framework import serializers
from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    is_adult = serializers.SerializerMethodField()

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

    def get_is_adult(self, obj):
        return obj.age >= 21 if obj.age is not None else None
