from rest_framework import serializers
from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    is_adult = serializers.ReadOnlyField()

    class Meta:
        model = Musician
        fields = "__all__"
        extra_kwargs = {
            "first_name": {"required": False},
            "last_name": {"required": False},
            "instrument": {"required": False},
        }
