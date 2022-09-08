from musician.models import Musician

from rest_framework import serializers


class MusicianSerializer(serializers.ModelSerializer):

    class Meta:
        model = Musician
        fields = ("first_name", "last_name", "instrument",
                  "age", "date_of_applying", "is_adult")
