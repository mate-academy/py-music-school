from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from musician.models import Musician


class MusicianSerializer(ModelSerializer):
    class Meta:
        model = Musician
        fields = (
            "id",
            "first_name",
            "last_name",
            "instrument",
            "age",
            "date_of_applying",
        )


class MusicianDetailSerializer(MusicianSerializer):
    is_adult = serializers.BooleanField()

    class Meta(MusicianSerializer.Meta):
        MusicianSerializer.Meta.fields += ("is_adult",)
