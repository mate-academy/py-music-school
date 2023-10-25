from rest_framework import serializers

from musician.models import Musician


class MusicianNonGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = "__all__"


class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = (
            "id", "first_name", "last_name", "instrument", "age", "is_adult"
        )
