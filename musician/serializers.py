from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError as DRFValidationError

from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField(min_value=14)
    is_adult = serializers.CharField(read_only=True)

    class Meta:
        model = Musician
        fields = "__all__"
