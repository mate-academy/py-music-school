from rest_framework import serializers

from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = "__all__"


class MusicianListSerializer(MusicianSerializer):
    is_adult = serializers.CharField(
        source="musician.is_adult",
        read_only=True
    )

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


class MusicianDetailSerializer(MusicianSerializer):
    full_name = serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        model = Musician
        fields = (
            "id",
            "first_name",
            "last_name",
            "full_name",
            "instrument",
            "age",
            "date_of_applying",
        )
