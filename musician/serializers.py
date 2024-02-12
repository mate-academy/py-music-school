from rest_framework import serializers

from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = ("id", "first_name", "last_name", "age", "instrument", "is_adult")
