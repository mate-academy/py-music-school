from rest_framework import viewsets

from musician.models import Musician
from musician.serializers import MusicianSerializer


class MusicianViewSet(viewsets.ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer

    def get_queryset(self):
        return Musician.objects.all()

    def get_serializer_class(self):
        return MusicianSerializer
