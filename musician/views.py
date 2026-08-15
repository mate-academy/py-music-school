from rest_framework import viewsets
from musician.models import Musician
from musician.serializers import MusicianSerializer


class MusicianViewSet(viewsets.ViewSet):
    request = Musician.objects.all()
    serializer_clas = MusicianSerializer

    