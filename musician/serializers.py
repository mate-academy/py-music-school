from rest_framework import serializers

from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):

    # def validate(self, attrs):
    #     data = super(MusicianSerializer, self).validate(attrs)
    #     if attrs["age"] < 14:
    #         raise serializers.ValidationError({
    #             "age": "age must be greater than 14"
    #         })
    #     return data

    class Meta:
        model = Musician
        fields = ("first_name",
                  "last_name",
                  "instrument",
                  "age",
                  "date_of_applying",
                  "is_adult")

        read_only_fields = ("is_adult",)
