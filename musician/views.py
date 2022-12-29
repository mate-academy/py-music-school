from rest_framework import viewsets

from musician.models import Musician
from musician.serializers import MusicianSerializer, MusicianGetSerializer


class MusicianViewSet(viewsets.ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer

    def get_serializer_class(self):
        if self.action in ("list",):
            return MusicianGetSerializer

        return MusicianSerializer
