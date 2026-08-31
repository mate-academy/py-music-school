from rest_framework import serializers
from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    is_adult = serializers.ReadOnlyField()

    class Meta:
        model = Musician
        fields = "__all__"

    def validate_age(self, age):
        if age < 14:
            raise serializers.ValidationError("Age must be between 14 and 18")
        return age
