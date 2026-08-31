from rest_framework.serializers import ModelSerializer
from .models import Musician


class MusicianSerializer(ModelSerializer):
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
