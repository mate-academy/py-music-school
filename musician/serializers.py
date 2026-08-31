from rest_framework.serializers import ModelSerializer

from musician.models import Musician


class MusicianSerializer(ModelSerializer):
    class Meta:
        model = Musician
        fields = [
            "first_name",
            "last_name",
            "instrument",
            "age",
            "is_adult",
        ]
