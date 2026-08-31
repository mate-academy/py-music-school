from rest_framework import serializers

from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        data = super(MusicianSerializer, self).validate(attrs)
        if "age" in attrs:
            Musician.validate_age(attrs["age"], serializers.ValidationError)
        return data

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
