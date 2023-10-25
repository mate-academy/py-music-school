from rest_framework import viewsets

from musician.models import Musician
from musician.serializers import MusicianSerializer, MusicianNonGetSerializer


class MusicianViewSet(viewsets.ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return MusicianSerializer

        return MusicianNonGetSerializer
