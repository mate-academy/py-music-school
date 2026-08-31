from rest_framework import viewsets

from musician.serializers import MusicianSerializer
from musician.models import Musician


class MusicianViewSet(viewsets.ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
