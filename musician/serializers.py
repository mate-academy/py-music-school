from rest_framework import serializers
from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=63)
    last_name = serializers.CharField(max_length=63)
    instrument = serializers.CharField(max_length=63)
    age = serializers.IntegerField()
    date_of_applying = serializers.DateField()

    class Meta:
        model = Musician
        fields = "__all__"

    def create(self, validated_data):
        return Musician.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get(
            "first_name",
            instance.first_name)
        instance.last_name = validated_data.get(
            "last_name",
            instance.last_name)
        instance.instrument = validated_data.get(
            "instrument",
            instance.instrument)
        instance.age = validated_data.get("age", instance.age)
        instance.date_of_applying = validated_data.get(
            "retired",
            instance.date_of_applying)
        instance.save()
        return instance
