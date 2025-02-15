from musician.models import Musician
from musician.serializers import MusicianSerializer
from rest_framework import viewsets


class MusicianSet(viewsets.ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
