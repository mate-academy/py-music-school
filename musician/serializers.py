from rest_framework import serializers
from musician.models import Musician
from .constants import FIELDS_MUSICIAN


class MusicianSerializer(serializers.ModelSerializer):

    class Meta:
        model = Musician
        fields = FIELDS_MUSICIAN
