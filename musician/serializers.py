from rest_framework import serializers
from .models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        # property is_adult will be added as read-only field
        fields = [
            "first_name",
            "last_name",
            "instrument",
            "age",
            "date_of_applying",
            "is_adult"
        ]
