from typing import Type

from rest_framework import viewsets
from rest_framework.serializers import Serializer

from musician.models import Musician
from musician.serializers import (
    MusicianSerializer,
    MusicianListSerializer,
    MusicianDetailSerializer,
)


class MusicianViewSet(viewsets.ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer

    def get_serializer_class(self) -> Type[Serializer]:
        if self.action == "list":
            return MusicianListSerializer
        return MusicianDetailSerializer
