from rest_framework import serializers

from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField(min_value=14)
    is_adult = serializers.BooleanField(read_only=True)

    class Meta:
        model = Musician
        fields = "__all__"
