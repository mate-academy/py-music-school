from rest_framework import serializers, status
from rest_framework.response import Response

from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):

    class Meta:
        model = Musician
        fields = (
            "id",
            "first_name",
            "last_name",
            "instrument",
            "age",
            "date_of_applying",
            "is_adult",
        )
