from rest_framework import viewsets
from .models import Musician
from musician.serializers import MusicianSerializer


class MusicianViewSet(viewsets.ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
