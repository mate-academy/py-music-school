from rest_framework import serializers, viewsets, mixins

from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):

    class Meta:
        model = Musician
        fields = (
            "id",
            "first_name",
            "last_name",
            "instrument",
            "age",
            "date_of_applying",
            "is_adult",
        )


class MusicianViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
