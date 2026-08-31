from rest_framework import serializers

from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    date_of_applying = serializers.DateField(read_only=True)
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
            "is_adult"
        )

    def get_is_adult(self, obj: Musician) -> bool:
        return obj.is_adult
