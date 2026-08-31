from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet

from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = ("id", "first_name", "last_name", "instrument", "age",
                  "is_adult")
