from rest_framework import serializers

from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        data = super(MusicianSerializer, self).validate(attrs)
        if attrs.get("age"):
            Musician.validate_age(
                attrs["age"], 14, serializers.ValidationError
            )
        return data

    class Meta:
        model = Musician
        fields = ("first_name", "last_name", "instrument", "age", "is_adult")
