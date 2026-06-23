from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from musician.models import Musician


class MusicianSerializer(ModelSerializer):
    age = serializers.IntegerField(min_value=14)

    class Meta:
        model = Musician
        fields = ["id",
                  "first_name",
                  "last_name",
                  "instrument",
                  "age",
                  "date_of_applying",
                  "is_adult"]
