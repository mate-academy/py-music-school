from rest_framework import viewsets

from musician.models import Musician
from musician.serializers import MusicianSerializer


class MusicianView(viewsets.ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
