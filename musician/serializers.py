from rest_framework import serializers

from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    is_adult = serializers.SerializerMethodField()

    class Meta:
        model = Musician
        fields = "__all__"
        read_only_fiels = ("id", "date_of_applying", "is_adult")

    def get_is_adult(self, obj):
        return obj.is_adult
