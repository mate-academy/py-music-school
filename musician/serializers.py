from rest_framework import serializers

from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    is_adult = serializers.SerializerMethodField()

    class Meta:
        model = Musician
        fields = [
            "id",
            "first_name",
            "last_name",
            "instrument",
            "age",
            "is_adult",
            "date_of_applying",
        ]
        read_only_fields = ["id", "date_of_applying", "is_adult"]

    def get_is_adult(self, obj):
        return obj.is_adult
