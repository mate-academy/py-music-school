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
            "date_of_applying",
            "is_adult"
        ]

    def get_is_adult(self, obj):
        return obj.is_adult

    def create(self, validated_data):
        musician = Musician.objects.create(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            instrument=validated_data["instrument"],
            age=validated_data["age"]
        )
        return musician

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get(
            "first_name",
            instance.first_name
        )
        instance.last_name = validated_data.get(
            "last_name",
            instance.last_name
        )
        instance.instrument = validated_data.get(
            "instrument",
            instance.instrument
        )
        instance.age = validated_data.get("age", instance.age)
        instance.save()
        return instance
