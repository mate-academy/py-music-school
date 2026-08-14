from rest_framework.viewsets import ModelViewSet

from musician.serializers import (
    MusicianSerializer,
    Musician,
)


class MusicianViewSet(ModelViewSet):
    queryset = Musician.objects
    serializer_class = MusicianSerializer
