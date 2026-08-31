from rest_framework import viewsets

from musician.models import Musician
from musician.serializers import MusicianSerializer


class MusicianViewSet(viewsets.ModelViewSet):
    serializer_class = MusicianSerializer
    queryset = Musician.objects.all()
