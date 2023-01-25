from rest_framework import serializers

from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = ("id", "first_name", "last_name", "instrument", "age",
                  "date_of_applying", "is_adult",)
        read_only_fields = ("is_adult",)

    def validate(self, attrs):
        data = super().validate(attrs)
        if "age" in attrs and attrs["age"] < 14:
            raise serializers.ValidationError({
                "age": "We do not accept people who are under 14"
            })
        return data
