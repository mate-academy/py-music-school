from rest_framework import serializers

from musician.models import Musician


class MusicianSerializer(serializers.Serializer):
    class Meta:
        model = Musician
        fields = (
            "first_name",
            "last_name",
            "instrument",
            "age",
            "date_of_applying",
        )


class MusicianListSerializer(MusicianSerializer):
    is_adult = serializers.IntegerField(source="musician.is_adult", read_only=True)

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


class MusicianDetailSerializer(MusicianSerializer):
    is_adult = serializers.IntegerField(source="musician.is_adult", read_only=False)

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
