from rest_framework import viewsets

from musician.models import Musician
from musician.serializers import MusicianSerializer


class MusicianView(viewsets.ModelViewSet):
    serializer_class = MusicianSerializer
    queryset = Musician.objects.all()
