from rest_framework import serializers
from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    is_adult = serializers.ReadOnlyField()
    date_of_applying = serializers.DateField(read_only=True)

    class Meta:
        model = Musician
        fields = "__all__"
        read_only_fields = ("date_of_applying", "is_adult")
