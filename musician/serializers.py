from rest_framework import serializers

from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    is_adult = serializers.ReadOnlyField(read_only=True)

    class Meta:
        model = Musician
        fields = "__all__"

    @staticmethod
    def validate_age(data):
        if data < 14:
            raise serializers.ValidationError()
        return data
