from rest_framework import serializers

from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    instrument = serializers.IntegerField(required=True)
    age = serializers.IntegerField(required=True)
    date_of_applying = serializers.DateField(required=True)

    class Meta:
        model = Musician
        fields = [
            "id",
            "first_name",
            "last_name",
            "instrument",
            "age",
            "date_of_applying",
            "is_adult"
        ]
